// strings.go
package main

import (
	"fmt"
	"strings"
)

func main() {
	var s string

	fmt.Printf("文字列を入力してください:")
	fmt.Scan(&s)

	// 文字をカウントする。
	fmt.Printf("%sの文字数は%d¥n", s, strings.Count(s, "")-1)

	// 文字列を繰り返す。
	fmt.Printf("%sを2回繰り返すと%s¥n", s, strings.Repeat(s, 2))

	// すべて大文字に変換する。
	fmt.Printf("%sの小文字を大文字にすると%s¥n", s, strings.ToUpper(s))

	// すべて小文字に変換する。
	fmt.Printf("%sの大文字を小文字にすると%s¥n", s, strings.ToLower(s))
}
