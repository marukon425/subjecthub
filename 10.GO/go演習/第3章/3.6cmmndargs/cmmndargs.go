// cmndargs.go
package main

import (
	"fmt"
	"os"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("引数を2個指定してください。")
		os.Exit(1)
	}

	fmt.Printf("実行ファイル名: %s¥n", os.Args[0])
	fmt.Printf("引数1: %s¥n", os.Args[1])
	fmt.Printf("引数2: %s¥n", os.Args[2])
}
