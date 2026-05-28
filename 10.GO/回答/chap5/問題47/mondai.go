package main

import (
	"fmt"
)

func main() {

	pref := make(map[string]float64)

	pref["青森県"] = 124.9
	pref["岩手県"] = 122.9
	pref["宮城県"] = 96.6
	pref["秋田県"] = 238.6
	pref["山形県"] = 188.0
	pref["福島県"] = 184.4

	for key, value := range pref {
		fmt.Printf("%s の人口は %.1f 万人です\n", key, value)
	}
}
