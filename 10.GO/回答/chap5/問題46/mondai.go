package main

import (
	"fmt"
)

func createEvenList(list []int) []int {
	var numlist []int

	for _, num := range list {
		if num%2 == 0 {
			numlist = append(numlist, num)
		}
	}

	return numlist
}

func createOddList(list []int) []int {
	var numlist []int

	for _, num := range list {
		if num%2 != 0 {
			numlist = append(numlist, num)
		}
	}

	return numlist
}

func main() {
	list := []int{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

	evenList := createEvenList(list)
	oddList := createOddList(list)

	fmt.Println("list = ", list)
	fmt.Println("偶数値のリスト = ", evenList)
	fmt.Println("奇数値のリスト = ", oddList)
}
