package main

import (
	"html/template"
	"net/http"
	"strconv"
	"strings"
)

const (
	kuro  = "黒"
	shiro = "白"
	size  = 8 // 8×8のオセロ盤
)

// Board：8×8のマス目
type Board [size][size]string

// ViewData：テンプレートに渡すデータ
type ViewData struct {
	Turn       string          // 現在の手番
	Board      *Board          // 盤面
	GameOver   bool            // ゲーム終了フラグ
	Winner     string          // 勝者（引き分けは空文字）
	KuroCount  int             // 黒の石の数
	ShiroCount int             // 白の石の数
	ValidMoves map[string]bool // 置ける場所のセット（キー: "行_列"）
	MustPass   bool            // パス強制フラグ
}

var tmpl = template.Must(template.ParseFiles("game.tmpl"))

func (v *ViewData) Execute(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	if err := tmpl.Execute(w, v); err != nil {
		panic(err)
	}
}

// 手番を切り替えるマップ（"" はゲーム開始時）
var nextTurnMap = map[string]string{
	kuro:  shiro,
	shiro: kuro,
	"":    kuro, // 黒が先手
}

func turnFormValue(r *http.Request) (string, string) {
	turn := r.FormValue("turn")
	return turn, nextTurnMap[turn]
}

// boardFormValue：盤面を復元する
// GET リクエスト時はオセロの初期配置（中央に4石）をセット
func boardFormValue(r *http.Request) *Board {
	var board Board
	if r.Method == "GET" {
		board[3][3] = shiro
		board[3][4] = kuro
		board[4][3] = kuro
		board[4][4] = shiro
		return &board
	}
	// POST 時は hidden input から盤面を復元
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			name := "c" + strconv.Itoa(row) + "_" + strconv.Itoa(col)
			board[row][col] = r.FormValue(name)
		}
	}
	return &board
}

// オセロの8方向（縦・横・斜め）
var dirs = [8][2]int{
	{-1, -1}, {-1, 0}, {-1, 1},
	{0, -1}, {0, 1},
	{1, -1}, {1, 0}, {1, 1},
}

func opponentOf(turn string) string {
	if turn == kuro {
		return shiro
	}
	return kuro
}

// flippable：(row, col) に turn を置いたとき、ひっくり返せる石の座標リストを返す
// オセロのルール：相手の石を自分の石で挟める場合のみ着手できる
func flippable(b *Board, row, col int, turn string) [][2]int {
	if b[row][col] != "" {
		return nil // すでに石がある場所には置けない
	}
	opp := opponentOf(turn)
	var result [][2]int

	for _, d := range dirs {
		var line [][2]int
		r, c := row+d[0], col+d[1]
		// 相手の石が続く間進む
		for r >= 0 && r < size && c >= 0 && c < size && b[r][c] == opp {
			line = append(line, [2]int{r, c})
			r += d[0]
			c += d[1]
		}
		// 相手の石の先に自分の石があれば、lineの石をすべてひっくり返せる
		if len(line) > 0 && r >= 0 && r < size && c >= 0 && c < size && b[r][c] == turn {
			result = append(result, line...)
		}
	}
	return result
}

// getValidMoves：turn が置ける全マスを "行_列" をキーとしたマップで返す
func getValidMoves(b *Board, turn string) map[string]bool {
	moves := make(map[string]bool)
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			if len(flippable(b, row, col, turn)) > 0 {
				moves[strconv.Itoa(row)+"_"+strconv.Itoa(col)] = true
			}
		}
	}
	return moves
}

// applyMove：(row, col) に stone を置き、ひっくり返した後の新しい盤面を返す
func applyMove(b *Board, row, col int, turn string) *Board {
	nb := *b // 値コピーして新しい盤面を作る
	nb[row][col] = turn
	for _, pos := range flippable(b, row, col, turn) {
		nb[pos[0]][pos[1]] = turn
	}
	return &nb
}

// countStones：盤面の黒と白の石数を数える
func countStones(b *Board) (int, int) {
	k, s := 0, 0
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			switch b[row][col] {
			case kuro:
				k++
			case shiro:
				s++
			}
		}
	}
	return k, s
}

func gameHandle(w http.ResponseWriter, r *http.Request) {
	turn, nextTurn := turnFormValue(r)
	board := boardFormValue(r)

	// POST かつ有効な手なら盤面に反映
	if r.Method == "POST" {
		move := r.FormValue("move")
		if move != "" && move != "pass" && turn != "" {
			parts := strings.Split(move, "_")
			if len(parts) == 2 {
				row, errR := strconv.Atoi(parts[0])
				col, errC := strconv.Atoi(parts[1])
				if errR == nil && errC == nil {
					board = applyMove(board, row, col, turn)
				}
			}
		}
	}

	// 次のプレイヤーが置けるマスを計算
	validMoves := getValidMoves(board, nextTurn)
	mustPass := len(validMoves) == 0
	gameOver := false
	winner := ""

	if mustPass {
		// 相手（今動いたプレイヤー）も置けない → 両者パス不能でゲーム終了
		if len(getValidMoves(board, opponentOf(nextTurn))) == 0 {
			gameOver = true
			mustPass = false
			k, s := countStones(board)
			if k > s {
				winner = kuro
			} else if s > k {
				winner = shiro
			}
			// k == s のときは引き分け（winner = ""）
		}
	}

	k, s := countStones(board)
	v := ViewData{
		Turn:       nextTurn,
		Board:      board,
		GameOver:   gameOver,
		Winner:     winner,
		KuroCount:  k,
		ShiroCount: s,
		ValidMoves: validMoves,
		MustPass:   mustPass,
	}
	v.Execute(w)
}

func main() {
	http.HandleFunc("/game", gameHandle)
	if err := http.ListenAndServe(":4000", nil); err != nil {
		panic(err)
	}
}
