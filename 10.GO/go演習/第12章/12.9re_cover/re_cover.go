package main

import (
	"fmt"
)

func main() {
	var x int

	fmt.Printf("整数>")
	fmt.Scan(&x)

	defer func() {
		p := recover()
		if p != nil {
			fmt.Println("安全に終了します")
		}
	}()

	z := 100 / x //xが0のときにパニックが発生する

	fmt.Print("100 / %d = %d\n", x, z)
}
