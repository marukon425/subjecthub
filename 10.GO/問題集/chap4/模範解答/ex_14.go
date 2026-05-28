/**
continue 文
１から１０００までの合計を求めるが
キーボードから入力された倍数を除く合計を求める
*/
package main

import "fmt"

func main() {
	// 変数 total（合計値）の初期化、型 int
	var total int = 0
	// 変数 mod（倍数）の宣言、型 int
	var mod int

	// キーボードから倍数を入力し変数 mod に保存
	// 入力促進
	fmt.Print("倍数を入力 = ")
	// 入力
	fmt.Scan(&mod)

	// １から１０００までの入力された倍数を除く合計を求める
	for i := 1; i <= 1000; i++ {
		// 入力された倍数か否かを判断
		if i%mod != 0 {
			// 入力された倍数だったら処理をスキップ
			total += i
		}
		// 合計を求める
		//total += i
	}

	// 入力された倍数を除く合計を表示
	fmt.Printf("１から１０００までの、%d の倍数を除く合計 = %d\n", mod, total)
}
