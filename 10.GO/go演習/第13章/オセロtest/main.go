package main

import (
	"encoding/json"
	"html/template"
	"math"
	"net/http"
	"strconv"
	"strings"
)

const (
	kuro = "黒"
	shiro = "白"
	size  = 8
)

type Board [size][size]string

type ViewData struct {
	Turn        string
	Board       *Board
	GameOver    bool
	Winner      string
	KuroCount   int
	ShiroCount  int
	ValidMoves  map[string]bool
	MustPass    bool
	History     []BoardSnapshot
	Mode        string // "pvp" or "pvc"
	AIDiff      string // "easy" "normal" "hard"
	LastMove    string // "行_列" or ""
	FlippedJSON string // JSON array of "行_列" for flip animation
	HintMode    bool
}

type BoardSnapshot struct {
	Board      Board
	Turn       string
	KuroCount  int
	ShiroCount int
}

var tmpl = template.Must(template.New("game.tmpl").Funcs(template.FuncMap{
	"add1": func(i int) int { return i + 1 },
	"not":  func(b bool) bool { return !b },
}).ParseFiles("game.tmpl"))

func (v *ViewData) Execute(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	if err := tmpl.Execute(w, v); err != nil {
		panic(err)
	}
}

var nextTurnMap = map[string]string{
	kuro:  shiro,
	shiro: kuro,
	"":    kuro,
}

func opponentOf(turn string) string {
	if turn == kuro {
		return shiro
	}
	return kuro
}

var dirs = [8][2]int{
	{-1, -1}, {-1, 0}, {-1, 1},
	{0, -1}, {0, 1},
	{1, -1}, {1, 0}, {1, 1},
}

func flippable(b *Board, row, col int, turn string) [][2]int {
	if b[row][col] != "" {
		return nil
	}
	opp := opponentOf(turn)
	var result [][2]int
	for _, d := range dirs {
		var line [][2]int
		r, c := row+d[0], col+d[1]
		for r >= 0 && r < size && c >= 0 && c < size && b[r][c] == opp {
			line = append(line, [2]int{r, c})
			r += d[0]
			c += d[1]
		}
		if len(line) > 0 && r >= 0 && r < size && c >= 0 && c < size && b[r][c] == turn {
			result = append(result, line...)
		}
	}
	return result
}

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

func applyMove(b *Board, row, col int, turn string) (*Board, [][2]int) {
	nb := *b
	nb[row][col] = turn
	flipped := flippable(b, row, col, turn)
	for _, pos := range flipped {
		nb[pos[0]][pos[1]] = turn
	}
	return &nb, flipped
}

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

// --- AI (Minimax + Alpha-Beta) ---

// 位置価値テーブル（角・辺・危険マスを考慮）
var posWeight = [8][8]int{
	{100, -20, 10, 5, 5, 10, -20, 100},
	{-20, -40, -5, -5, -5, -5, -40, -20},
	{10, -5, 1, 1, 1, 1, -5, 10},
	{5, -5, 1, 0, 0, 1, -5, 5},
	{5, -5, 1, 0, 0, 1, -5, 5},
	{10, -5, 1, 1, 1, 1, -5, 10},
	{-20, -40, -5, -5, -5, -5, -40, -20},
	{100, -20, 10, 5, 5, 10, -20, 100},
}

func evaluate(b *Board, aiTurn string) int {
	opp := opponentOf(aiTurn)
	k, s := countStones(b)
	total := k + s

	// 序盤〜中盤は位置価値＋手数優先、終盤は石数優先
	if total >= 54 {
		if aiTurn == kuro {
			return (k - s) * 10
		}
		return (s - k) * 10
	}

	score := 0
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			w := posWeight[row][col]
			if b[row][col] == aiTurn {
				score += w
			} else if b[row][col] == opp {
				score -= w
			}
		}
	}
	// 合法手数の差（手数が多いほど有利）
	myMoves := len(getValidMoves(b, aiTurn))
	oppMoves := len(getValidMoves(b, opp))
	score += (myMoves - oppMoves) * 5
	return score
}

func minimax(b *Board, depth int, alpha, beta int, maximizing bool, aiTurn string) int {
	currentTurn := aiTurn
	if !maximizing {
		currentTurn = opponentOf(aiTurn)
	}
	moves := getValidMoves(b, currentTurn)

	if depth == 0 || (len(moves) == 0 && len(getValidMoves(b, opponentOf(currentTurn))) == 0) {
		return evaluate(b, aiTurn)
	}

	if len(moves) == 0 {
		// パス：相手のターンへ
		return minimax(b, depth-1, alpha, beta, !maximizing, aiTurn)
	}

	if maximizing {
		best := math.MinInt32
		for key := range moves {
			parts := strings.Split(key, "_")
			row, _ := strconv.Atoi(parts[0])
			col, _ := strconv.Atoi(parts[1])
			nb, _ := applyMove(b, row, col, currentTurn)
			val := minimax(nb, depth-1, alpha, beta, false, aiTurn)
			if val > best {
				best = val
			}
			if val > alpha {
				alpha = val
			}
			if beta <= alpha {
				break
			}
		}
		return best
	} else {
		best := math.MaxInt32
		for key := range moves {
			parts := strings.Split(key, "_")
			row, _ := strconv.Atoi(parts[0])
			col, _ := strconv.Atoi(parts[1])
			nb, _ := applyMove(b, row, col, currentTurn)
			val := minimax(nb, depth-1, alpha, beta, true, aiTurn)
			if val < best {
				best = val
			}
			if val < beta {
				beta = val
			}
			if beta <= alpha {
				break
			}
		}
		return best
	}
}

func aiDepth(diff string) int {
	switch diff {
	case "easy":
		return 1
	case "hard":
		return 6
	default: // normal
		return 3
	}
}

func bestAIMove(b *Board, aiTurn string, diff string) (int, int) {
	moves := getValidMoves(b, aiTurn)
	depth := aiDepth(diff)
	bestVal := math.MinInt32
	bestRow, bestCol := -1, -1
	for key := range moves {
		parts := strings.Split(key, "_")
		row, _ := strconv.Atoi(parts[0])
		col, _ := strconv.Atoi(parts[1])
		nb, _ := applyMove(b, row, col, aiTurn)
		val := minimax(nb, depth-1, math.MinInt32, math.MaxInt32, false, aiTurn)
		if val > bestVal {
			bestVal = val
			bestRow, bestCol = row, col
		}
	}
	return bestRow, bestCol
}

// --- セッション管理（メモリ内）---
// 簡易実装：クッキーIDをキーにしてhistoryを持つ
var sessions = map[string][]BoardSnapshot{}

func sessionID(r *http.Request) string {
	c, err := r.Cookie("othello_session")
	if err != nil {
		return ""
	}
	return c.Value
}

func generateID() string {
	return strconv.FormatInt(int64(len(sessions)+1)*12345, 36)
}

func gameHandle(w http.ResponseWriter, r *http.Request) {
	r.ParseForm()

	mode := r.FormValue("mode")
	if mode == "" {
		mode = "pvp"
	}
	aiDiff := r.FormValue("ai_diff")
	if aiDiff == "" {
		aiDiff = "normal"
	}
	hintMode := r.FormValue("hint_mode") == "1"

	// undo
	undoReq := r.FormValue("undo") == "1"

	// セッション
	sid := sessionID(r)
	if sid == "" || r.Method == "GET" {
		sid = generateID()
		http.SetCookie(w, &http.Cookie{Name: "othello_session", Value: sid, Path: "/"})
		sessions[sid] = nil
	}

	// 盤面・手番の復元
	var board *Board
	var turn string
	var flippedCells [][2]int
	lastMove := ""

	if r.Method == "GET" {
		// 初期化
		var b Board
		b[3][3] = shiro
		b[3][4] = kuro
		b[4][3] = kuro
		b[4][4] = shiro
		board = &b
		turn = kuro
		sessions[sid] = nil
	} else {
		// POST: フォームから盤面復元
		var b Board
		for row := 0; row < size; row++ {
			for col := 0; col < size; col++ {
				b[row][col] = r.FormValue("c" + strconv.Itoa(row) + "_" + strconv.Itoa(col))
			}
		}
		board = &b
		turn = r.FormValue("turn")
		if turn == "" {
			turn = kuro
		}

		if undoReq {
			hist := sessions[sid]
			if len(hist) >= 2 {
				// 2手戻す（自分の手番に戻る）
				target := hist[len(hist)-2]
				sessions[sid] = hist[:len(hist)-2]
				nb := target.Board
				board = &nb
				turn = target.Turn
			} else if len(hist) == 1 {
				target := hist[0]
				sessions[sid] = nil
				nb := target.Board
				board = &nb
				turn = target.Turn
			}
		} else {
			// 着手処理
			move := r.FormValue("move")
			if move != "" && move != "pass" && turn != "" {
				parts := strings.Split(move, "_")
				if len(parts) == 2 {
					row, errR := strconv.Atoi(parts[0])
					col, errC := strconv.Atoi(parts[1])
					if errR == nil && errC == nil && len(flippable(board, row, col, turn)) > 0 {
						// 着手前の状態をhistoryに保存
						k0, s0 := countStones(board)
						sessions[sid] = append(sessions[sid], BoardSnapshot{
							Board: *board, Turn: turn, KuroCount: k0, ShiroCount: s0,
						})
						board, flippedCells = applyMove(board, row, col, turn)
						lastMove = move
						turn = nextTurnMap[turn]
					}
				}
			}
		}
	}

	// 次の手番の合法手を計算
	validMoves := getValidMoves(board, turn)
	mustPass := len(validMoves) == 0
	gameOver := false
	winner := ""

	if mustPass {
		if len(getValidMoves(board, opponentOf(turn))) == 0 {
			gameOver = true
			mustPass = false
			k, s := countStones(board)
			if k > s {
				winner = kuro
			} else if s > k {
				winner = shiro
			}
		}
	}

	// AI のターンなら自動着手
	if !gameOver && !mustPass && mode == "pvc" && turn == shiro && !undoReq {
		aiRow, aiCol := bestAIMove(board, shiro, aiDiff)
		if aiRow >= 0 {
			k0, s0 := countStones(board)
			sessions[sid] = append(sessions[sid], BoardSnapshot{
				Board: *board, Turn: turn, KuroCount: k0, ShiroCount: s0,
			})
			board, flippedCells = applyMove(board, aiRow, aiCol, shiro)
			lastMove = strconv.Itoa(aiRow) + "_" + strconv.Itoa(aiCol)
			turn = kuro

			// AI着手後の合法手を再計算
			validMoves = getValidMoves(board, turn)
			mustPass = len(validMoves) == 0
			if mustPass {
				if len(getValidMoves(board, opponentOf(turn))) == 0 {
					gameOver = true
					mustPass = false
					k, s := countStones(board)
					if k > s {
						winner = kuro
					} else if s > k {
						winner = shiro
					}
				}
			}
		}
	}

	// AI パス処理
	if !gameOver && mustPass && mode == "pvc" && turn == shiro {
		turn = kuro
		validMoves = getValidMoves(board, turn)
		mustPass = false
	}

	// flippedCells を JSON に変換
	flippedStrs := []string{}
	for _, pos := range flippedCells {
		flippedStrs = append(flippedStrs, strconv.Itoa(pos[0])+"_"+strconv.Itoa(pos[1]))
	}
	flippedJSON, _ := json.Marshal(flippedStrs)

	k, s := countStones(board)
	v := ViewData{
		Turn:        turn,
		Board:       board,
		GameOver:    gameOver,
		Winner:      winner,
		KuroCount:   k,
		ShiroCount:  s,
		ValidMoves:  validMoves,
		MustPass:    mustPass,
		History:     sessions[sid],
		Mode:        mode,
		AIDiff:      aiDiff,
		LastMove:    lastMove,
		FlippedJSON: string(flippedJSON),
		HintMode:    hintMode,
	}
	v.Execute(w)
}

func main() {
	http.HandleFunc("/game", gameHandle)
	if err := http.ListenAndServe(":4001", nil); err != nil {
		panic(err)
	}
}
