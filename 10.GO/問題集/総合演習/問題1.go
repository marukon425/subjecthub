package main

import (
	"fmt"
)

// 構造体 CarToy の定義
type CarToy struct {
	name   string
	code   string
	outlet string
	price  int
}

// 構造体 TrainToy の定義
type TrainToy struct {
	name   string
	code   string
	outlet string
	price  int
}

// メソッド displayToyの定義
// レシーバ：CarToy
//
//	↓ これがレシーバ(構造体にメソッドをくっつける仕組み)
func (toy CarToy) displayToy() {
	fmt.Println("おもちゃの名前：", toy.name)
	fmt.Println("色", toy.code)
	fmt.Println("販売店", toy.outlet)
	fmt.Println("価格：", toy.price)
}

func (toy CarToy) run() {
	fmt.Println("車のおもちゃが走ります：ブロロロロー")
}

func (toy TrainToy) displayToy() {
	fmt.Println("おもちゃの名前：", toy.name)
	fmt.Println("色", toy.code)
	fmt.Println("販売店", toy.outlet)
	fmt.Println("価格：", toy.price)
}
func (toy TrainToy) run() {
	fmt.Println("電車のおもちゃが走ります：ガタンゴトン")
}

func main() {
	CarToy := CarToy{
		name:   "車のおもちゃ",
		code:   "CAR001",
		outlet: "トミー",
		price:  1200,
	}

	TrainToy := TrainToy{
		name:   "電車のおもちゃ",
		code:   "TRAIN001",
		outlet: "トミー",
		price:  2800,
	}

	CarToy.displayToy()
	CarToy.run()
	fmt.Println()

	TrainToy.displayToy()
	TrainToy.run()
	fmt.Println()

}
