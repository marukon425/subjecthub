package main

import (
	"fmt"
	"math"
)

// Point 型の定義
type Point struct{ X, Y int }

// Distance - 2点間の距離を求めるメソッド
func (p Point) Distance(q Point) int {
	d := math.Sqrt(float64((p.X-q.X)*(p.X-q.X)) + float64((p.Y-q.Y)*(p.Y-q.Y)))
	return int(d)
}

func main() {
	p1 := Point{5, 5}
	p2 := Point{8, 9}

	fmt.Printf("%vと%vの距離は%d\n", p1, p2, p1.Distance(p2))
}
