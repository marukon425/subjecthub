package main

import "fmt"

// 参照渡しの関数
func byVal(a int) {
	a = a + 1
}

func main() {
	// 値渡しの呼び出し
	var n = 1
	byVal(n)
	fmt.Println("n = ", n) // n = 1のまま

	// 参照渡しの呼び出し
	byVal(n)
	fmt.Println("n = ", n) // n = 2に変更される
}
