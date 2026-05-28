// animal.go
package main

import "fmt"

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

func main() {
	// 犬と猫を作る
	dog := new(Dog)
	cat := new(Cat)
	// 犬と猫が鳴く
	dog.Cry()
	cat.Cry()
	// 犬と猫のスライスを作る
	animals := [...]Animal{dog, cat}
	// 犬と猫が鳴く
	for _, a := range animals {
		a.Cry()
	}
}
