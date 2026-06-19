package main

import "fmt"

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

func (toy Toy) displayToy() {
	fmt.Println("おもちゃの名前:", toy.name)
	fmt.Println("商品コード:", toy.code)
}

func (toy CarToy) displayToy() {
	toy.Toy.displayToy()
	fmt.Println("販売店:", toy.outlet)
	fmt.Println("価格:", toy.price)
}

func (toy TrainToy) displayToy() {
	toy.Toy.displayToy()
	fmt.Println("販売店:", toy.outlet)
	fmt.Println("価格:", toy.price)
}

func (toy CarToy) run() {
	fmt.Println("車のおもちゃが走ります：ブロロロロー")
}

func (toy TrainToy) run() {
	fmt.Println("電車のおもちゃが走ります：ガタンゴトン")
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

	carToy.displayToy()
	carToy.run()
	fmt.Println()

	trainToy.displayToy()
	trainToy.run()
}
