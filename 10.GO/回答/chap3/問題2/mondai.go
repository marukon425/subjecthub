package main

import (
	"fmt"
)

func main() {
	var data1, data2 int32

	var addAns, subAns, mulAns, modAns int32

	var divAns float32

	fmt.Println("2つの数を入力してください")
	fmt.Print("1目の数を入力")
	fmt.Scan(&data1)
	fmt.Println("2つ目の数を入力")
	fmt.Scan(&data2)

	addAns = data1 + data2
	subAns = data1 - data2
	mulAns = data1 * data2
	modAns = data1 / data2
	divAns = float32(data1 % data2)

	fmt.Println("足し算: %s", addAns)
	fmt.Println("引き算: %s", subAns)
	fmt.Println("割り算: %s", mulAns)
	fmt.Println("掛け算: %s", modAns)
	fmt.Println("剰余: %s", divAns)
}
