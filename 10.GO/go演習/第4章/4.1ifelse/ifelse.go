package main

import "fmt"

// 条件式
func main() {
	var x int

	fmt.Printf("整数を入力してください")
	fmt.Scan(&x)

	if x > 0 {
		fmt.Printf("%dは正の数です。", x)
	} else if x < 0 {
		fmt.Printf("%dは負の数です。", x)
	} else {
		fmt.Printf("%dはゼロです", x)
	}

}
