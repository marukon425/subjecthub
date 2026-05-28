package main

import "fmt"

func main() {
	var name string
	fmt.Println("あなたの名前を入力してください")
	fmt.Scanln(&name)
	fmt.Printf("こんにちは、%s！\n", name)
}
