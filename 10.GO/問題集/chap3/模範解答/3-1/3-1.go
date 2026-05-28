// 3-1.go
/*
三角形の面積を求めて表示する
*/

package main

import "fmt"

func main() {
	// 底辺と高さを入力
	var bottom, height float64
	// 面積を宣言
	var area float64

	// キーボードから底辺と高さを入力
	fmt.Print("底辺 = ")
	fmt.Scan(&bottom)
	fmt.Print("高さ = ")
	fmt.Scan(&height)
	// 面積を計算
	area = (bottom * height) / 2
	// 結果を表示
	fmt.Printf("三角形の面積 =  %7.3f\n", area)
}
