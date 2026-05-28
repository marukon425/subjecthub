package main

import "fmt"

func main() {
	var total int = 0
	var mod int

	fmt.Printf("倍数を入力 = ")
	fmt.Scan(&mod)
	for i := 1; i <= 1000; i++ {
		if i%mod == 0 {
			continue
		}
		total += i
	}
	fmt.Printf("1から100までの、%d の倍数を除く合計 = %d\n", mod, total)
}
