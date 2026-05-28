package main

import "fmt"

func main() {

	prefecture := map[string]float64{
		"青森県": 124.9,
		"岩手県": 122.9,
		"宮城県": 96.6,
		"福島県": 138.6,
		"山形県": 108.9,
		"福岡県": 184.8,
	}

	fmt.Println("登録されている県と人口")
	for name, pop := range prefecture {
		fmt.Printf("%s の人口は %.1f 万人です\n", name, pop)
	}

	var key string
	fmt.Print("確認したい県 = ")
	fmt.Scanln(&key)

	if pop, ok := prefecture[key]; ok {
		fmt.Printf("%s の人口は %.1f 万人です\n", key, pop)
	} else {
		fmt.Printf("%s は登録されていません\n", key)
	}
}
