package main

import "fmt"

type Person struct {
	name string
	age  byte
}

func main() {
	var basicData = []Person{}

	basicData = append(basicData, Person{"鈴木一郎", 38})
	basicData = append(basicData, Person{"広瀬すず", 22})
	basicData = append(basicData, Person{"土方歳三", 36})

	fmt.Println(basicData)
}
