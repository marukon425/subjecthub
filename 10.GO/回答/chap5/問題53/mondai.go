package main

import "fmt"

func main() {

	list := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10} // (1)

	var total int = 0
	var evenNumber int = 0
	var oddNumber int = 0

	for _, num := range list {
		total += num
		if num%2 == 0 {
			evenNumber++
		} else {
			oddNumber++
		}
	}

	fmt.Println("list = ", list)
	fmt.Println("リストの合計 = ", total)
	fmt.Println("偶数の数 = ", evenNumber)
	fmt.Println("奇数の数 = ", oddNumber)
	fmt.Println("インデックス番号2から8までの切り出し", list[2:8]) // (2)
}
