package main

import "fmt"

// インターフェースの定義
type ToyProc interface {
	displayToy()
	run()
}

type Toy struct {
	name string
	code string
}

type CarToy struct {
	Toy
	outlet string
	price  int
}

type TrainToy struct {
	Toy
	outlet string
	price  int
}

func (toy *Toy) displayToy() {
	fmt.Println("おもちゃの名前：" + toy.name)
	fmt.Println("商品コード：" + toy.code)
}

func (toy *Toy) run() {
	fmt.Println("おもちゃが走ります")
}

func (toy *CarToy) displayToy() {
	toy.Toy.displayToy()
	fmt.Println("販売店：" + toy.outlet)
	fmt.Printf("価格：%d\n", toy.price)
}

func (toy *CarToy) run() {
	fmt.Println("車のおもちゃ が走ります：ブロロロロー")
}

func (toy *TrainToy) displayToy() {
	toy.Toy.displayToy()
	fmt.Println("販売店：" + toy.outlet)
	fmt.Printf("価格：%d 円\n", toy.price)
}

func (toy *TrainToy) run() {
	fmt.Println("電車のおもちゃ が走ります：ガタンゴトン！！")
}

func main() {
	carToy := CarToy{
		Toy:    Toy{name: "車のおもちゃ", code: "CAR001"},
		outlet: "トミー",
		price:  1200,
	}

	trainToy := TrainToy{
		Toy:    Toy{name: "電車のおもちゃ", code: "TRAIN001"},
		outlet: "トミー",
		price:  2800,
	}

	var toyProc ToyProc

	toyProc = &carToy
	toyProc.displayToy()
	toyProc.run()
	fmt.Println()

	toyProc = &trainToy
	toyProc.displayToy()
	toyProc.run()
	fmt.Println()
}
