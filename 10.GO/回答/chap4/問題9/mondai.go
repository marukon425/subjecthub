package main

import (
	"fmt"
)

func main() {
	var limit int
	var total int = 0
	fmt.Printf("1から250までの奇数の合計")
	fmt.Scan(&limit)

	for i := 1; i < limit; i++ {
		if i%2 == 1 {
			total += i
		}
	}
	fmt.Printf("1から%dまでの合計 = %d", limit, total)
}
