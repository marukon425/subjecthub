// circ.go
package main

import (
	"fmt"
	"math"
)

// 面積と円周を返す関数
func circle(r float64) (float64, float64) {
	area := r * r * 3.14
	circ := 2 * math.Pi * r
	return area, circ
}

func main() {
	var r float64
	fmt.Printf("半径を入力してください:")
	fmt.Scan(&r)

	var area, circ = circle(r)
	fmt.Printf("半径%fの面積は%f\n", r, area)
	fmt.Printf("半径%fの円周は%f\n", r, circ)
}
