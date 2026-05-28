package main

import (
	"bufio"
	"fmt"
	"os"
)

func main()  {
	var height, weight float64
	
	fmt.Print("身長(cm 単位)を入力")
	fmt.Scan(height)

	fmt.Print("体重(kg 単位)を入力")
	fmt.Scan(weight)

	heightM := 

	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()


	bmi := weight / (heightM * heightM)
}