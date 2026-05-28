package main

import "fmt"

func main() {
	var n int
	var v float32
	var name string

	fmt.Printf("整数を入力してください:")
	fmt.Scan(&n)

	fmt.Printf("実数を入力してください:")
	fmt.Scan(&v)

	fmt.Printf("文字列を入力してください:")
	fmt.Scan(&name)

	fmt.Printf("nの値は=%d¥n", n)
	fmt.Printf("vの値は=%8.3f¥n", v)
	fmt.Printf("nameは=%s¥n", name)
}
