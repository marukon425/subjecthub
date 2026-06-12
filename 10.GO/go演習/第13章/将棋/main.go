package main

import (
	"encoding/json"
	"html/template"
	"log"
	"math/rand"
	"net/http"
)

const boardSize = 9

// 駒の種類
const (
	Empty = ""
	Fu    = "FU" // 歩兵
	Ky    = "KY" // 香車
	Ke    = "KE" // 桂馬
	Gi    = "GI" // 銀将
	Ki    = "KI" // 金将
	Ka    = "KA" // 角行
	Hi    = "HI" // 飛車
	Ou    = "OU" // 王将/玉将
)

type Piece struct {
	Type     string `json:"type"`
	Owner    int    `json:"owner"`    // 0=先手(下), 1=後手(上)
	Promoted bool   `json:"promoted"`
}

type Move struct {
	FromRow int    `json:"fromRow"`
	FromCol int    `json:"fromCol"`
	ToRow   int    `json:"toRow"`
	ToCol   int    `json:"toCol"`
	Drop    bool   `json:"drop"`
	Piece   string `json:"piece"`
	Promote bool   `json:"promote"`
}

type GameState struct {
	Board    [boardSize][boardSize]*Piece `json:"board"`
	Turn     int                         `json:"turn"` // 0=先手, 1=後手
	Hand     [2]map[string]int           `json:"hand"` // 持ち駒
	GameOver bool                        `json:"gameOver"`
	Winner   int                         `json:"winner"`
	Message  string                      `json:"message"`
	Mode     string                      `json:"mode"` // "pvp" or "pvc"
	Check    bool                        `json:"check"`
}

var game *GameState

func newGame(mode string) *GameState {
	g := &GameState{
		Mode: mode,
		Turn: 0,
	}
	g.Hand[0] = make(map[string]int)
	g.Hand[1] = make(map[string]int)
	g.setupBoard()
	return g
}

func (g *GameState) setupBoard() {
	// 後手(上、owner=1)の初期配置
	back1 := []string{Ky, Ke, Gi, Ki, Ou, Ki, Gi, Ke, Ky}
	for col, t := range back1 {
		g.Board[0][col] = &Piece{Type: t, Owner: 1}
	}
	g.Board[1][7] = &Piece{Type: Hi, Owner: 1}
	g.Board[1][1] = &Piece{Type: Ka, Owner: 1}
	for col := 0; col < 9; col++ {
		g.Board[2][col] = &Piece{Type: Fu, Owner: 1}
	}

	// 先手(下、owner=0)の初期配置
	back9 := []string{Ky, Ke, Gi, Ki, Ou, Ki, Gi, Ke, Ky}
	for col, t := range back9 {
		g.Board[8][col] = &Piece{Type: t, Owner: 0}
	}
	g.Board[7][1] = &Piece{Type: Hi, Owner: 0}
	g.Board[7][7] = &Piece{Type: Ka, Owner: 0}
	for col := 0; col < 9; col++ {
		g.Board[6][col] = &Piece{Type: Fu, Owner: 0}
	}
}

// 成れるか判定
func canPromote(p *Piece, fromRow, toRow int) bool {
	if p.Promoted || p.Type == Ki || p.Type == Ou {
		return false
	}
	if p.Owner == 0 {
		return fromRow <= 2 || toRow <= 2
	}
	return fromRow >= 6 || toRow >= 6
}

// 成らなければならないか
func mustPromote(p *Piece, toRow int) bool {
	if p.Promoted {
		return false
	}
	if p.Owner == 0 {
		if p.Type == Fu || p.Type == Ky {
			return toRow == 0
		}
		if p.Type == Ke {
			return toRow <= 1
		}
	} else {
		if p.Type == Fu || p.Type == Ky {
			return toRow == 8
		}
		if p.Type == Ke {
			return toRow >= 7
		}
	}
	return false
}

// 駒の移動可能マスを計算
func (g *GameState) getLegalMoves(row, col int) [][2]int {
	p := g.Board[row][col]
	if p == nil {
		return nil
	}
	var moves [][2]int
	dirs := g.getMoveDirections(p)

	for _, d := range dirs {
		dr, dc, sliding := d[0], d[1], d[2] == 1
		r, c := row+dr, col+dc
		for r >= 0 && r < 9 && c >= 0 && c < 9 {
			target := g.Board[r][c]
			if target != nil {
				if target.Owner != p.Owner {
					moves = append(moves, [2]int{r, c})
				}
				break
			}
			moves = append(moves, [2]int{r, c})
			if !sliding {
				break
			}
			r += dr
			c += dc
		}
	}

	// 動けない場所に行ってしまう手を除外
	var legal [][2]int
	for _, m := range moves {
		if !mustPromote(p, m[0]) || canPromote(p, row, m[0]) {
			// 動かした後に自分の王が詰んでないかチェック
			if !g.wouldBeInCheck(row, col, m[0], m[1], false, p.Owner) {
				legal = append(legal, m)
			}
		} else if mustPromote(p, m[0]) {
			if !g.wouldBeInCheck(row, col, m[0], m[1], true, p.Owner) {
				legal = append(legal, m)
			}
		}
	}
	return legal
}

// 駒の移動方向を返す [dr, dc, sliding(0/1)]
func (g *GameState) getMoveDirections(p *Piece) [][3]int {
	up := -1
	if p.Owner == 1 {
		up = 1
	}

	if p.Promoted {
		switch p.Type {
		case Fu, Ky, Ke, Gi:
			// 金将と同じ動き
			return [][3]int{{up, 0, 0}, {up, -1, 0}, {up, 1, 0}, {0, -1, 0}, {0, 1, 0}, {-up, 0, 0}}
		case Ka:
			// 竜馬: 角+近傍1マス
			return [][3]int{{1, 1, 1}, {1, -1, 1}, {-1, 1, 1}, {-1, -1, 1}, {1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}}
		case Hi:
			// 竜王: 飛+近傍斜め1マス
			return [][3]int{{1, 0, 1}, {-1, 0, 1}, {0, 1, 1}, {0, -1, 1}, {1, 1, 0}, {1, -1, 0}, {-1, 1, 0}, {-1, -1, 0}}
		}
	}

	switch p.Type {
	case Fu:
		return [][3]int{{up, 0, 0}}
	case Ky:
		return [][3]int{{up, 0, 1}}
	case Ke:
		return [][3]int{{up * 2, -1, 0}, {up * 2, 1, 0}}
	case Gi:
		return [][3]int{{up, 0, 0}, {up, -1, 0}, {up, 1, 0}, {-up, -1, 0}, {-up, 1, 0}}
	case Ki:
		return [][3]int{{up, 0, 0}, {up, -1, 0}, {up, 1, 0}, {0, -1, 0}, {0, 1, 0}, {-up, 0, 0}}
	case Ka:
		return [][3]int{{1, 1, 1}, {1, -1, 1}, {-1, 1, 1}, {-1, -1, 1}}
	case Hi:
		return [][3]int{{1, 0, 1}, {-1, 0, 1}, {0, 1, 1}, {0, -1, 1}}
	case Ou:
		return [][3]int{{1, 0, 0}, {-1, 0, 0}, {0, 1, 0}, {0, -1, 0}, {1, 1, 0}, {1, -1, 0}, {-1, 1, 0}, {-1, -1, 0}}
	}
	return nil
}

// 指定プレイヤーの王の位置を返す
func (g *GameState) findKing(owner int) (int, int) {
	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			p := g.Board[r][c]
			if p != nil && p.Owner == owner && p.Type == Ou {
				return r, c
			}
		}
	}
	return -1, -1
}

// 指定マスが敵に攻撃されているか
func (g *GameState) isAttacked(row, col, byOwner int) bool {
	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			p := g.Board[r][c]
			if p == nil || p.Owner != byOwner {
				continue
			}
			dirs := g.getMoveDirections(p)
			for _, d := range dirs {
				dr, dc, sliding := d[0], d[1], d[2] == 1
				nr, nc := r+dr, c+dc
				for nr >= 0 && nr < 9 && nc >= 0 && nc < 9 {
					if nr == row && nc == col {
						return true
					}
					if g.Board[nr][nc] != nil {
						break
					}
					if !sliding {
						break
					}
					nr += dr
					nc += dc
				}
			}
		}
	}
	return false
}

// 動かした後に王が王手になるか
func (g *GameState) wouldBeInCheck(fromR, fromC, toR, toC int, promote bool, owner int) bool {
	// 一時的に動かす
	orig := g.Board[toR][toC]
	p := g.Board[fromR][fromC]
	if promote {
		np := &Piece{Type: p.Type, Owner: p.Owner, Promoted: true}
		g.Board[toR][toC] = np
	} else {
		g.Board[toR][toC] = p
	}
	g.Board[fromR][fromC] = nil

	kr, kc := g.findKing(owner)
	inCheck := false
	if kr >= 0 {
		inCheck = g.isAttacked(kr, kc, 1-owner)
	}

	// 戻す
	g.Board[fromR][fromC] = p
	g.Board[toR][toC] = orig
	return inCheck
}

// 打ち駒の合法手
func (g *GameState) getDropMoves(pieceType string, owner int) [][2]int {
	var moves [][2]int
	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			if g.Board[r][c] != nil {
				continue
			}
			p := &Piece{Type: pieceType, Owner: owner}
			if mustPromote(p, r) {
				continue
			}
			// 二歩チェック
			if pieceType == Fu {
				hasFu := false
				for rr := 0; rr < 9; rr++ {
					pp := g.Board[rr][c]
					if pp != nil && pp.Owner == owner && pp.Type == Fu && !pp.Promoted {
						hasFu = true
						break
					}
				}
				if hasFu {
					continue
				}
			}
			// 打ち歩詰めチェック (簡易)
			moves = append(moves, [2]int{r, c})
		}
	}
	return moves
}

// 手を実行
func (g *GameState) applyMove(m Move) bool {
	if m.Drop {
		if g.Hand[m.FromRow][m.Piece] <= 0 {
			return false
		}
		g.Board[m.ToRow][m.ToCol] = &Piece{Type: m.Piece, Owner: m.FromRow}
		g.Hand[m.FromRow][m.Piece]--
	} else {
		p := g.Board[m.FromRow][m.FromCol]
		if p == nil || p.Owner != g.Turn {
			return false
		}
		captured := g.Board[m.ToRow][m.ToCol]
		if captured != nil {
			baseType := captured.Type
			g.Hand[g.Turn][baseType]++
		}
		if m.Promote || mustPromote(p, m.ToRow) {
			g.Board[m.ToRow][m.ToCol] = &Piece{Type: p.Type, Owner: p.Owner, Promoted: true}
		} else {
			g.Board[m.ToRow][m.ToCol] = p
		}
		g.Board[m.FromRow][m.FromCol] = nil

		// 王を取った場合
		if captured != nil && captured.Type == Ou {
			g.GameOver = true
			g.Winner = g.Turn
			return true
		}
	}

	// 王手判定
	oppKr, oppKc := g.findKing(1 - g.Turn)
	if oppKr >= 0 && g.isAttacked(oppKr, oppKc, g.Turn) {
		g.Check = true
		g.Message = "王手！"
	} else {
		g.Check = false
		g.Message = ""
	}

	g.Turn = 1 - g.Turn
	return true
}

// CPU(後手)の手をランダムに選ぶ (簡易AI)
func (g *GameState) cpuMove() {
	type moveOption struct {
		move Move
		score int
	}
	var options []moveOption

	for r := 0; r < 9; r++ {
		for c := 0; c < 9; c++ {
			p := g.Board[r][c]
			if p == nil || p.Owner != 1 {
				continue
			}
			moves := g.getLegalMoves(r, c)
			for _, m := range moves {
				score := 0
				target := g.Board[m[0]][m[1]]
				if target != nil {
					score = pieceValue(target.Type)
				}
				promote := false
				if canPromote(p, r, m[0]) {
					promote = true
					score += 5
				}
				options = append(options, moveOption{
					Move{FromRow: r, FromCol: c, ToRow: m[0], ToCol: m[1], Promote: promote},
					score,
				})
			}
		}
	}

	// 持ち駒の打ち
	for pt, cnt := range g.Hand[1] {
		if cnt <= 0 {
			continue
		}
		drops := g.getDropMoves(pt, 1)
		for _, d := range drops {
			options = append(options, moveOption{
				Move{FromRow: 1, Drop: true, Piece: pt, ToRow: d[0], ToCol: d[1]},
				pieceValue(pt) / 2,
			})
		}
	}

	if len(options) == 0 {
		g.GameOver = true
		g.Winner = 0
		g.Message = "後手が投了しました。先手の勝ちです！"
		return
	}

	// 最高スコアの手を選ぶ (同スコアはランダム)
	maxScore := -1
	for _, o := range options {
		if o.score > maxScore {
			maxScore = o.score
		}
	}
	var best []moveOption
	for _, o := range options {
		if o.score == maxScore {
			best = append(best, o)
		}
	}
	chosen := best[rand.Intn(len(best))]
	g.applyMove(chosen.move)
}

func pieceValue(t string) int {
	switch t {
	case Fu:
		return 1
	case Ky, Ke:
		return 3
	case Gi:
		return 5
	case Ki:
		return 6
	case Ka:
		return 8
	case Hi:
		return 10
	case Ou:
		return 100
	}
	return 0
}

var tmpl *template.Template

func main() {
	tmpl = template.Must(template.ParseFiles("game.tmpl"))
	game = newGame("pvc")

	http.HandleFunc("/", handleIndex)
	http.HandleFunc("/state", handleState)
	http.HandleFunc("/move", handleMove)
	http.HandleFunc("/reset", handleReset)
	http.HandleFunc("/legal", handleLegal)
	http.HandleFunc("/drop", handleDrop)

	log.Println("将棋サーバー起動: http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}

func handleIndex(w http.ResponseWriter, r *http.Request) {
	tmpl.Execute(w, nil)
}

func handleState(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(game)
}

func handleMove(w http.ResponseWriter, r *http.Request) {
	var m Move
	json.NewDecoder(r.Body).Decode(&m)
	w.Header().Set("Content-Type", "application/json")

	if game.GameOver || game.Turn != 0 {
		json.NewEncoder(w).Encode(game)
		return
	}

	// 合法手チェック
	if !m.Drop {
		legal := game.getLegalMoves(m.FromRow, m.FromCol)
		found := false
		for _, l := range legal {
			if l[0] == m.ToRow && l[1] == m.ToCol {
				found = true
				break
			}
		}
		if !found {
			json.NewEncoder(w).Encode(map[string]string{"error": "illegal move"})
			return
		}
	}

	game.applyMove(m)

	if !game.GameOver && game.Mode == "pvc" && game.Turn == 1 {
		game.cpuMove()
	}

	json.NewEncoder(w).Encode(game)
}

func handleReset(w http.ResponseWriter, r *http.Request) {
	var req struct {
		Mode string `json:"mode"`
	}
	json.NewDecoder(r.Body).Decode(&req)
	if req.Mode == "" {
		req.Mode = "pvc"
	}
	game = newGame(req.Mode)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(game)
}

func handleLegal(w http.ResponseWriter, r *http.Request) {
	var req struct {
		Row int `json:"row"`
		Col int `json:"col"`
	}
	json.NewDecoder(r.Body).Decode(&req)
	moves := game.getLegalMoves(req.Row, req.Col)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(moves)
}

func handleDrop(w http.ResponseWriter, r *http.Request) {
	var req struct {
		Piece string `json:"piece"`
		Owner int    `json:"owner"`
	}
	json.NewDecoder(r.Body).Decode(&req)
	moves := game.getDropMoves(req.Piece, req.Owner)
	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(moves)
}
