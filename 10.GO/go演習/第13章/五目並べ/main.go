package main

import (
	"html/template"
	"net/http"
	"strconv"
)

const maru, batsu = "〇", "×"

// 盤面サイズと勝利条件をまとめて定数で定義
// 変更したいときはここだけ変えればよい
const size = 15   // 五目並べは15×15マス
const winLen = 5  // 縦・横・斜めに5つ並んだら勝利

// Board：size×size のマス目を表す型
type Board [size][size]string

// ViewData：テンプレートへ渡すデータ
type ViewData struct {
	Turn   string
	Board  *Board
	Win    bool
	Draw   bool
	Winner string
}

var tmpl *template.Template = template.Must(template.ParseFiles("game.tmpl"))

func (v *ViewData) Execute(w http.ResponseWriter) {
	w.Header().Set("Content-Type", "text/html; charset=utf-8")
	if err := tmpl.Execute(w, v); err != nil {
		panic(err)
	}
}

// gameHandle："/game" へのリクエストを処理するハンドラ
func gameHandle(w http.ResponseWriter, r *http.Request) {
	turn, nextTurn := turnFormValue(r)
	board := boardFormValue(r)

	win, draw, winner := false, false, ""

	if turn != "" {
		win = board.win(turn)
		if win {
			winner = turn
			board.setBar()
		} else {
			draw = board.draw()
		}
	}

	v := ViewData{nextTurn, board, win, draw, winner}
	v.Execute(w)
}

// boardFormValue：フォームから盤面を復元する
// 15×15 のインデックスが2桁になるため、"c行_列" 形式（例：c14_3）を使う
func boardFormValue(r *http.Request) *Board {
	var board Board
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			name := "c" + strconv.Itoa(row) + "_" + strconv.Itoa(col)
			board[row][col] = r.FormValue(name)
		}
	}
	return &board
}

// nextTurnMap：手番を交互に切り替えるマップ
var nextTurnMap = map[string]string{
	maru:  batsu,
	batsu: maru,
	"":    maru,
}

func turnFormValue(r *http.Request) (string, string) {
	turn := r.FormValue("turn")
	nextTurn := nextTurnMap[turn]
	return turn, nextTurn
}

// win：縦・横・斜めの4方向について winLen 個連続しているか判定
// 三目並べのように勝利パターンを列挙する方法は15×15では現実的でないため、
// 全マスを起点にしてループで連続数を数える方式にしている
func (b *Board) win(turn string) bool {
	// チェックする4方向（右, 下, 右下斜め, 左下斜め）
	directions := [4][2]int{
		{0, 1},  // 横（右方向）
		{1, 0},  // 縦（下方向）
		{1, 1},  // 斜め（右下方向）
		{1, -1}, // 斜め（左下方向）
	}

	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			// 起点が turn と違うマスはスキップ
			if b[row][col] != turn {
				continue
			}
			// 各方向に向かって連続数を数える
			for _, d := range directions {
				count := 1
				for i := 1; i < winLen; i++ {
					r, c := row+d[0]*i, col+d[1]*i
					// 盤外 or 違う記号なら連続が切れた
					if r < 0 || r >= size || c < 0 || c >= size || b[r][c] != turn {
						break
					}
					count++
				}
				if count >= winLen {
					return true
				}
			}
		}
	}
	return false
}

// draw：全マスが埋まっていれば引き分け
func (b *Board) draw() bool {
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			if b[row][col] == "" {
				return false
			}
		}
	}
	return true
}

// setBar：勝利後に残った空マスを "-" で埋めてボタンを無効化する
func (b *Board) setBar() {
	for row := 0; row < size; row++ {
		for col := 0; col < size; col++ {
			if b[row][col] == "" {
				b[row][col] = "-"
			}
		}
	}
}

func main() {
	http.HandleFunc("/game", gameHandle)
	if err := http.ListenAndServe(":4000", nil); err != nil {
		panic(err)
	}
}
