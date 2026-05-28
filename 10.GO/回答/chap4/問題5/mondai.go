package main

import "fmt"

func main() {
	var data int32
	fmt.Print("整数値を入力¥n")
	fmt.Scan(&data)
	if data%2 == 0 {
		fmt.Printf("%dは偶数", data)
	} else {
		fmt.Printf("%dは奇数", data)
	}
}
