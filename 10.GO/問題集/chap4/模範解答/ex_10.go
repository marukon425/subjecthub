/**
ex_9.go において
上限の整数値を入力した後、さらに倍数を表す整数値を
キーボードから入力し、１から上限の整数までの入力された
倍数の合計を求めて表示する
*/
package main

import "fmt"

func main() {
	// 変数 limti（上限の整数） を宣言（型 int）
	var limit int
	// 変数 total（合計）を宣言（型 int）と 0 に初期化
	var total int = 0
	// 変数 mod （倍数）を宣言（型 int）
	var mod int

	// 上限の整数を入力
	// 入力促進
	fmt.Print("上限の整数を入力 = ")
	// キーボードから整数を入力し、変数 limit に保存
	fmt.Scan(&limit)

	// 倍数を入力
	// 入力促進
	fmt.Print("倍数を入力 = ")
	// キーボードから倍数を入力し、変数 mod に保存
	fmt.Scan(&mod)

	// １から上限の整数までの倍数の合計を求める
	for i := 1; i <= limit; i++ {
		if i%mod == 0 {
			total += i
		}
	}

	// 合計値を表示
	fmt.Printf("1 から %d までの %d の倍数の合計 = %d\n", limit, mod, total)
}
