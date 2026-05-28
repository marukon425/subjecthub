/**
無限ループ
キーボードから"END"が入力されるまで
文字列を入力し、表示し続ける
*/
package main

import "fmt"

func main() {
	// 変数 inputStr 宣言（型 string）
	var inputStr string

	// 無限ループ
	for {
		// 入力促進
		fmt.Print("文字列入力 = ")
		// キーボードから文字列を入力し、変数 inputStr に保存
		fmt.Scan(&inputStr)
		// 入力文字列が "END" か否かを判断
		if inputStr == "END" {
			// 入力文字列が "END" であれば無限ループを抜ける
			break
		}
		// 表示
		fmt.Println("出力 = ", inputStr)
	}
	// プログラム終了表示
	fmt.Println("プログラム終了")
}
