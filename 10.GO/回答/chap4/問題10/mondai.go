package main

import (
	"fmt"
)

func main() {
	var limit int
	var total int = 0
	var mod int = 0
	fmt.Printf("上限の整数を入力 =")
	fmt.Scan(&limit)
	fmt.Printf("倍数を入力")
	fmt.Scan(&mod)

	for i := 1; i <= limit; i++ {
		if i%mod == 0 {
			total += i
		}
	}
	fmt.Printf("1から%dまでの %d の倍数の合計 = %d\n", limit, mod, total)
}
