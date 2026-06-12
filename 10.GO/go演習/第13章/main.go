// package main：このファイルがプログラムの起点（エントリーポイント）であることを示す
package main

import (
	"html/template" // HTMLテンプレート（雛形ファイル）を扱うパッケージ
	"net/http"      // WebサーバーやHTTPリクエスト/レスポンスを扱うパッケージ
	"strconv"       // 数値と文字列を変換するパッケージ（例：0 → "0"）
)

// ゲームで使う記号を定数として定義
// const で複数の定数をまとめて宣言できる
const maru, batsu = "〇", "×"

// Board 型：3×3のマス目を表す型
// [3][3]string は「3行3列の string 配列」
// 各マスには "〇"・"×"・"-"・"" のいずれかが入る
type Board [3][3]string

// ViewData：HTMLテンプレートに渡すデータをまとめた構造体
// テンプレート側では {{ .Turn }} のように各フィールドを参照できる
type ViewData struct {
	Turn   string // 現在の手番（"〇" または "×"）
	Board  *Board // 盤面の状態（ポインタで渡す）
	Win    bool   // 誰かが勝ったか
	Draw   bool   // 引き分けか
	Winner string // 勝者の記号（勝ちが確定したとき "〇" or "×"）
}

// template.Must：テンプレートファイルの読み込みに失敗したらすぐパニック（強制終了）する
// ParseFiles でテンプレートファイル "game.tmpl" を読み込む
// var tmpl は「パッケージ変数」（関数の外で宣言するのでどこからでも使える）
var tmpl *template.Template = template.Must(template.ParseFiles("game.tmpl"))

// Execute：ViewData の内容をテンプレートに当てはめてHTMLをブラウザへ送るメソッド
// レシーバが *ViewData なので、ViewData のポインタから呼び出す
func (v *ViewData) Execute(w http.ResponseWriter) {
	// レスポンスヘッダーに文字コードを指定（日本語文字化け防止）
	w.Header().Set("Content-Type", "text/html; charset=utf-8")

	// テンプレートに v のデータを埋め込んで w（ブラウザ）へ書き出す
	// エラーが起きたら panic で強制終了
	if err := tmpl.Execute(w, v); err != nil {
		panic(err)
	}
}

// gameHandle："/game" にアクセスされたときに呼ばれる関数（ハンドラ）
// r からフォームの送信値を受け取り、勝敗判定して結果をブラウザへ返す
func gameHandle(w http.ResponseWriter, r *http.Request) {
	// フォームから「今の手番」と「次の手番」を取得
	turn, nextTurn := turnFormValue(r)

	// フォームから盤面データを取得（9マス分の文字列）
	board := boardFormValue(r)

	// 勝敗・引き分けの初期値をセット
	win, draw, winner := false, false, ""

	// turn が空文字でない = 誰かが手を打った後のリクエスト
	if turn != "" {
		// 今の手番のプレイヤーが勝っているか判定
		win = board.win(turn)

		if win {
			winner = turn    // 勝者を記録
			board.setBar()  // 空マスを "-" で埋めてボタンを無効化
		} else {
			// 勝っていなければ引き分け判定
			draw = board.draw()
		}
	}

	// ViewData を作成してテンプレートへ渡す
	// nextTurn を渡すのは「次の手番」をフォームに保持させるため
	v := ViewData{nextTurn, board, win, draw, winner}
	v.Execute(w)
}

// boardFormValue：フォームの値から Board を組み立てて返す関数
// フォームのname属性は "c行番号列番号"（例：c00, c01, c12）という命名規則
func boardFormValue(r *http.Request) *Board {
	var board Board // ゼロ値（全マスが ""）で初期化
	for row, rows := range board {
		for col, _ := range rows {
			// 例：row=1, col=2 → name = "c12"
			name := "c" + strconv.Itoa(row) + strconv.Itoa(col)
			// フォームから取得した値をマスに設定
			board[row][col] = r.FormValue(name)
		}
	}
	// & を付けてポインタとして返す（Board のコピーを避けるため）
	return &board
}

// nextTurnMap：手番を交互に切り替えるためのマップ（辞書）
// キーが「今の手番」、値が「次の手番」
// "" → "〇" はゲーム開始時（手番が未設定）の場合
var nextTurnMap = map[string]string{
	maru:  batsu, // 〇の次は×
	batsu: maru,  // ×の次は〇
	"":    maru,  // 最初の手番は〇
}

// turnFormValue：フォームから手番を取得し、現在・次の手番を返す関数
// 戻り値が2つ（多値返し）になっている
func turnFormValue(r *http.Request) (string, string) {
	turn := r.FormValue("turn")    // フォームの "turn" フィールドを取得
	nextTurn := nextTurnMap[turn]  // マップから次の手番を求める
	return turn, nextTurn
}

// winBoardIndexArray：勝利条件となるマスの組み合わせをすべて列挙した配列
// [...]は要素数を自動カウントするGoの書き方
// 各要素は「3マスの座標セット」：row（行）と col（列）のペアが3つ
var winBoardIndexArray = [...][3]struct{ row, col int }{
	// 横1行が揃ったケース（0行目・1行目・2行目）
	{{0, 0}, {0, 1}, {0, 2}},
	{{1, 0}, {1, 1}, {1, 2}},
	{{2, 0}, {2, 1}, {2, 2}},
	// 縦1列が揃ったケース（0列目・1列目・2列目）
	{{0, 0}, {1, 0}, {2, 0}},
	{{0, 1}, {1, 1}, {2, 1}},
	{{0, 2}, {1, 2}, {2, 2}},
	// 斜めが揃ったケース（左上→右下、右上→左下）
	{{0, 0}, {1, 1}, {2, 2}},
	{{0, 2}, {1, 1}, {2, 0}},
}

// win：指定した手番（turn）が盤面で勝利しているか判定するメソッド
// レシーバ *Board：Board 型の変数から呼び出せる
func (b *Board) win(turn string) bool {
	// すべての勝利パターンをループで確認
	for _, w := range winBoardIndexArray {
		// 3マスすべてが同じ turn の記号なら勝利
		if b[w[0].row][w[0].col] == turn &&
			b[w[1].row][w[1].col] == turn &&
			b[w[2].row][w[2].col] == turn {
			return true
		}
	}
	// どのパターンにも当てはまらなければ未勝利
	return false
}

// draw：盤面が引き分け（全マスが埋まっている）かどうかを判定するメソッド
func (b *Board) draw() bool {
	for row, rows := range b {
		for col, _ := range rows {
			// 空マスが1つでもあればまだゲーム続行 → 引き分けではない
			if b[row][col] == "" {
				return false
			}
		}
	}
	// 空マスがなければ引き分け
	return true
}

// setBar：勝利後に残っている空マスを "-" で埋めるメソッド
// これによりHTMLテンプレート側でボタンを非活性にできる
func (b *Board) setBar() {
	for row, rows := range b {
		for col, _ := range rows {
			if b[row][col] == "" {
				b[row][col] = "-" // 空マスを "-" に置き換え
			}
		}
	}
}

// main：プログラムのエントリーポイント（最初に実行される関数）
func main() {
	// "/game" というURLパスへのリクエストを gameHandle 関数で処理する
	http.HandleFunc("/game", gameHandle)

	// ポート4000番でWebサーバーを起動
	// nil はデフォルトのルーター（ServeMux）を使う指定
	if err := http.ListenAndServe(":4000", nil); err != nil {
		panic(err) // 起動失敗時は強制終了
	}
}
