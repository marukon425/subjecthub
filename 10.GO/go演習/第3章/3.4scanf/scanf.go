// scanf.go
package main

import "fmt"

func main() {
	var n, m int

	fmt.Printf("2つの整数を入力してください: ")
	fmt.Scanf("%d %d", &n, &m)
	fmt.Printf("%dと%dの合計は%d\n", n, m, n+m)
}
