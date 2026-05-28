/**
キーボードから整数値を入力し
偶数か奇数かを判断する
*/
package main

import "fmt"

func main() {
	// 変数 data の宣言（型 int32）
	var data int32

	// 入力促進
	fmt.Print("整数値を入力 = ")
	// キーボードから整数値を入力
	fmt.Scan(&data)

	// 整数値が偶数化奇数かを判断
	if data%2 == 0 {
		// 偶数だったら
		fmt.Printf("%d は偶数\n", data)
	} else {
		// 奇数だったら
		fmt.Printf("%d は奇数\n", data)
	}
}
