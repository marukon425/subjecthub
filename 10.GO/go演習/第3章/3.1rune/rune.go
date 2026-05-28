package main

import "fmt"

func main() {
	var r rune = 'あ'
	fmt.Printf("%c %q %d %x¥n", r, r, r, r)

	r = rune(0x3044)
	fmt.Printf("%c %q %d %x¥n", r, r, r, r)
}
