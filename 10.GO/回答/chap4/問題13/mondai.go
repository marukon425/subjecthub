package main

import "fmt"

func main() {
	var inputStr string

	for {
		fmt.Printf("文字列を入力 = ")
		fmt.Scan(&inputStr)
		if inputStr == "END" {
			break
		}
		fmt.Printf("出力 = ", inputStr)
	}
	fmt.Printf("プログラム終了")
}
