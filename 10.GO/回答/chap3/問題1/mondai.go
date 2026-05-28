package main

import "fmt"

func main() {
	var bottom, height float32
	var area float32

	fmt.Print("底辺を入力してください: ")
	fmt.Scan(&bottom)

	fmt.Print("高さを入力してください: ")
	fmt.Scan(&height)

	area = bottom * height / 2

	fmt.Printf("面積は %f です\n", area)
}
