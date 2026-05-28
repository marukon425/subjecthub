/**
キーボードから得点を入力し
成績の評価を表示する
但し、得点の評価は以下のとおりとする
	90点以上　Sランク
	80点以上　Aランク
	70点以上　Bランク
	50点以上　Cランク
	40点以上　Dランク
	40点未満　不合格
*/
package main

import "fmt"

func main() {
	// 変数 score（得点）を宣言（型　int32）
	var score int32
	// 変数 evaluation（評価の文字列）を宣言（型　string）
	var evaluation string

	// キーボードから得点を入力
	// 入力促進
	fmt.Print("得点を入力 = ")
	// キーボードから得点を入力し変数 score に保存
	fmt.Scan(&score)

	// 得点を評価
	switch true {
	case score >= 90:
		evaluation = "Sランク"
	case score >= 80:
		evaluation = "Aランク"
	case score >= 70:
		evaluation = "Bランク"
	case score >= 50:
		evaluation = "Cランク"
	case score >= 40:
		evaluation = "Dランク"
	default:
		evaluation = "不合格"
	}

	// 成績評価を表示
	fmt.Printf("成績の評価は、%s です。\n", evaluation)
}
