// animal.go / animal2.go / animal3.go / その他
package main

import (
	"fmt"
	"math"
)

// Animal - 動物のインターフェース
type Animal interface {
	Cry()
}

// Dog - 犬の構造体
type Dog struct{}

// Cry - 犬が吠える
func (d *Dog) Cry() {
	fmt.Println("わんわん")
}

// Cat - 猫の構造体
type Cat struct{}

// Cry - 猫が鳴く
func (c *Cat) Cry() {
	fmt.Println("にゃーご")
}

// Book - 本の構造体（Animal を実装しない例）
type Book struct{}

// Cry - なんでも鳴くものは鳴かせ、鳴かないものは鳴かない
func Cry(any interface{}) {
	a, ok := any.(Animal) // Animal であるか調べる
	if !ok {
		fmt.Println("鳴かないよ。")
		return
	}
	a.Cry()
}

// Point 型の定義
type Point struct{ X, Y int }

// Distance - 2点間の距離を求めるメソッド
func (p Point) Distance(q Point) int {
	d := math.Sqrt(float64((p.X-q.X)*(p.X-q.X)) +
		float64((p.Y-q.Y)*(p.Y-q.Y)))
	return int(d)
}

// Value 型の定義
type Value int

// Twice – 値を2倍にするメソッド
func (v Value) Twice() Value {
	return v * 2
}

func main() {
	// --- Value のテスト ---
	var n, m Value
	n = 1
	m = n.Twice()
	fmt.Printf("%dの2倍は%d\n", n, m)
	fmt.Printf("%dの2倍は%d\n", m, m.Twice())

	// --- Point のテスト ---
	p1 := Point{5, 5}
	p2 := Point{8, 9}
	fmt.Printf("%vと%vの距離は%d\n", p1, p2, p1.Distance(p2))

	// --- Animal のテスト ---
	dog := new(Dog)
	cat := new(Cat)
	book := new(Book)

	// スライスで鳴かせる
	animals := [...]Animal{dog, cat}
	for _, a := range animals {
		a.Cry()
	}

	// Cry 関数で鳴かせる（本は鳴かない）
	Cry(dog)
	Cry(cat)
	Cry(book)
}
