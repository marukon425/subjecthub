package main

import "fmt"

type Point struct {
	X, Y int
}

type Circle struct {
	Center Point
	Radius int
}

func main() {
	var c = Circle{Point{50, 50}, 70}

	fmt.Println(c)
	fmt.Printf("中心座標は(%d, %d)", c.Center.X, c.Center.Y)
	fmt.Printf("半径は%d", c.Radius)
}
