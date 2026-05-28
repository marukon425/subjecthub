package main

import (
	"fmt"
)

func arrayMax(list []int) int {
	num := list[0]

	for _, mnum := range list {
		if num < mnum {
			num = mnum
		}
	}
	return num
}

func arrayMin(list []int) int {
	num := list[0]

	for _, mnum := range list {
		if num > mnum {
			num = mnum
		}
	}
	return num
}

func main() {
	numlist := []int{-10, 23, -55, 95, -45, 88, 9, -99, 123, 42}

	max := arrayMax(numlist)
	min := arrayMin(numlist)

	fmt.Printf("numlist = %v\n", numlist)
	fmt.Printf("最大値 = %d¥n", max)
	fmt.Printf("最小値 = %d¥n", min)
}
