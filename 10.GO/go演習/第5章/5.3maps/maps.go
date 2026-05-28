package main

import "fmt"

func main() {
	// マップリテラルからマップを作る
	var m1 = map[string]int{"Pochi": 5, "Kenta": 3, "Sally": 5, "Tommy": 7}
	fmt.Println(m1) // マップ全体を出力する

	m1["Kenta"] = 4     //キーが"Kenta"の要素の値を変更する
	delete(m1, "Tommy") // キーがTommyの要素を削除する
	fmt.Println(m1)     // マップ全体を出力する

	fmt.Printf("Pochi=%d", m1["Pochi"]) // "Pochi"の値を出力する
	// make(でマップを作る)
	var m2 = make(map[string]int)

	// マップのメンバーを登録する
	m2["Tommy"] = 18
	m2["jhon"] = 22
	m2["太田"] = 32

	fmt.Println("m2") // マップ全体を出力する
}
