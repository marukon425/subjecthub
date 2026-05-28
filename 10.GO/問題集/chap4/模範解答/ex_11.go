/**
９９表を表示する
*/
package main

import "fmt"

func main() {
	// 行の繰り返し
	for i := 1; i < 10; i++ {
		// 列の繰り返し
		for j := 1; j < 10; j++ {
			// かけ算結果を表示
			fmt.Printf("%4d", i * j)
		}
		// 各行で改行する
		fmt.Printf("\n")
	}
}
