package main

import "fmt"

func main() {
	var x = 3

	fmt.Printf("%dの2倍は%d\n", x, twice(x))
	fmt.Printf("合計は%d\n", sum(1, 3, 5, 7, 9))

	max, min := maxmin(3, 1, 4, 1, 5, 9)
	fmt.Printf("最大値は%d、最小値は%d\n", max, min)
}

// 引数の値を2倍にして返す関数
func twice(n int) int {
	return n * 2
}

// 合計を返す関数
func sum(vals ...int) int {
	total := 0

	for _, value := range vals {
		total += value
	}
	return total
}

// 最大値と最小値を返す関数
func maxmin(vals ...int) (int, int) {
	max := vals[0]
	min := vals[0]

	for _, value := range vals {
		if value > max {
			max = value
		}
		if value < min {
			min = value
		}
	}
	return max, min
}
