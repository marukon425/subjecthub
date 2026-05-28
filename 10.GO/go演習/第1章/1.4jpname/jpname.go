package test

import "fmt"

func 名前表示(氏名 string) {
	fmt.Println("こんにちは、%sさん！", 氏名)
}

func main() {
	var 名前 string
	fmt.Println("名前を入力してください：")
	fmt.Scan(&名前)
	名前表示(名前)
}
