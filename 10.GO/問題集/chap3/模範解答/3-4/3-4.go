/**
キーボードから円の半径を入力し
円周と面積を求めて表示する
*/
package main

import "fmt"

// 円周率 PAI（定数）3.14159 の宣言
const PAI = 3.14159

func main() {
	// 変数 radius （半径）の宣言（型 float64）
	var radius float64

	// キーボードから半径を入力
	// 入力促進
	fmt.Print("半径を入力 = ")
	// キーボードから半径を入力し、変数 radius に保存
	fmt.Scan(&radius)

	// 円周を計算し、変数 circumference に保存
	circumference := radius * 2 * PAI
	// 面積を計算し、変数 area に保存
	area := radius * radius * PAI

	// 円周を表示
	fmt.Printf("円周 = %f\n", circumference)
	// 面積を表示
	fmt.Printf("面積 = %f\n", area)
	fmt.Print("")
}
