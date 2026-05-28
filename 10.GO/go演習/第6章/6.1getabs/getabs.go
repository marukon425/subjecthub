package main

import (
	"fmt"
	"math"
)

func main() {
	var x float64

	fmt.Print("数を入力してください: ")
	fmt.Scan(&x)

	fmt.Printf("%f の絶対値は %f です\n", x, math.Abs(x))
}
