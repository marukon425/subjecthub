package main

import "fmt"

func main() {
	var limit int
	var total int = 0

	fmt.Print("上限の整数を入力: ")
	fmt.Scan(&limit)

	for i := 1; i <= limit; i++ {
		total += i
	}

	fmt.Printf("1から%dまでの合計 = %d\n", limit, total)
}
