package main

import "fmt"

// Value 型の定義
type Value int

// Twice – 値を2倍にするメソッド
func (v Value) Twice() Value {
	return v * 2
}

func main() {
	var n, m Value

	n = 1
	m = n.Twice()

	fmt.Printf("%dの2倍は%d\n", n, m)
	fmt.Printf("%dの2倍は%d\n", m, m.Twice())
}
