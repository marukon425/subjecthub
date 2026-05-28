package main

import "fmt"

func main() {
	// 配列を宣言して初期化
	var a [5]int = [5]int{1, 3, 5, 7, 9}

	// 配列の各要素を出力する
	for i, v := range a {
		fmt.Printf("a[%d]=%d¥n", i, v)
	}

	a[1] = 0       // 2番目の要素の値を変更する
	a[3] = 0       // 4番目の要素の値を変更する
	fmt.Println(a) // 配列全体を出力する

	// 配列を作る
	var b [5]int
	b[1] = 99
	b[3] = 99
	fmt.Println(b) // 配列を出力する

}
