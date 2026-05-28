package main

import "fmt"

func main() {
	var list = [5]int{1, 2, 3, 4, 5}
	var totalint = 0
	var evenNumberint = 0
	var oddNumberint = 0

	// 要素の合計と偶数・奇数の合計
	for _, v := range list {
		totalint += v
		if v%2 == 0 {
			evenNumberint += v
		} else {
			oddNumberint += v
		}
	}

	fmt.Println("list = ", list)
	fmt.Println("リストの合計 = ", totalint)
	fmt.Println("偶数値の合計 = ", evenNumberint)
	fmt.Println("奇数値の合計 = ", oddNumberint)
}
