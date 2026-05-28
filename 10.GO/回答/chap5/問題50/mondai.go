package main

import "fmt"

func main() {

	/**
	 * make 関数によって map を生成して変数 prefecture に代入
	 * key の型 string（県名）
	 * value の型 float（県の人口）
	 */
	prefecture := make(map[string]float64)

	/**
	 * 基地地方の県の県名と人口をキーボードから入力し
	 * マップ prefecture に保存する
	 */
	for i := 0; i < 6; i++ {
		var name string
		var pop float64

		fmt.Print("県名を入力してください：")
		fmt.Scan(&name)

		fmt.Print("人口（万人）を入力してください：")
		fmt.Scan(&pop)

		prefecture[name] = pop
	}

	/**
	 * for-range 文を使用して、map から県名と人口を取り出し表示
	 */
	for name, pop := range prefecture {
		fmt.Printf("%s の人口は %.1f 万人です\n", name, pop)
	}
}
