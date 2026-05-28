package main

import "fmt"

func Printmsgs(args ...interface{}) {
	fmt.Println(args...)
}

type Dog struct {
	name string
	age  int
}

func main() {
	Printmsgs("わんこだよ")
	Printmsgs(88, "わんこだよ")
	Printmsgs(-1, "わんこだ", "だめだこりゃ")

	dog := Dog{"Pochi", 12}

	Printmsgs(dog, "わんこだよ")
}
