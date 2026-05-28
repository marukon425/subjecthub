/**
キーボードから整数を入力し
１からその入力した整数までの整数値の合計を求めて
表示する
*/
package main

import "fmt"

func main() {
	// 変数 limti（上限の整数） を宣言（型 int）
	var limit int
	// 変数 total（合計）を宣言（型 int）と 0 に初期化
	var total int = 0

	// 上限の整数を入力
	// 入力促進
	fmt.Print("上限の整数を入力 = ")
	// キーボードから整数を入力し、変数 limit に保存
	fmt.Scan(&limit)

	// １から上限の整数までの整数値の合計を求める
	for i := 1; i <= limit; i++ {
		total += i
	}

	// 合計値を表示
	fmt.Printf("1 から %d までの合計 = %d\n", limit, total)
}
