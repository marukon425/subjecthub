package main

import (
	"fmt"
)

func main() {

	prefecture := make(map[string]float64)

	prefecture["青森県"] = 124.9
	prefecture["岩手県"] = 122.9
	prefecture["宮城県"] = 236.6
	prefecture["秋田県"] = 96.6
	prefecture["山形県"] = 109.3
	prefecture["福島県"] = 184.8

	for name, pop := range prefecture {
		fmt.Printf("%s の人口は %.1f 万人です\n", name, pop)
	}
}
