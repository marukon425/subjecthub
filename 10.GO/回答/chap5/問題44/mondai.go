package main

func arrayinfo(list []int) (int, int, int) {
	sum, evenCount, oddCount := 0, 0, 0

	// 配列の合計
	for _, v := range list {
		sum += v
		if v%2 == 0 {
			evenCount++
		} else {
			oddCount++
		}
	}

	return sum, evenCount, oddCount
}

func main() {
	list := []int{1, 2, 3, 4, 5}

	total, evenCount, oddCount := arrayinfo(list)

	println(total, evenCount, oddCount)
}
