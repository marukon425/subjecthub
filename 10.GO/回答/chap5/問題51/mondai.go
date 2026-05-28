package main

import "fmt"

func main() {

	prefecture := map[string]float64{
		"東京都": 124.9,
		"神奈川": 122.9,
		"大阪府": 96.6,
		"愛知県": 230.6,
		"北海道": 184.8,
	}

	fmt.Println("都道府県")

	for name, pop := range prefecture {
		fmt.Printf("%s の人口は %.1f 万人です\n", name, pop)
	}

	var key string
	fmt.Print("削除したい県 = ")
	fmt.Scanln(&key)

	delete(prefecture, key)

	fmt.Println("削除後")

	for name, pop := range prefecture {
		fmt.Printf("%s の人口は %.1f 万人です\n", name, pop)
	}
}
