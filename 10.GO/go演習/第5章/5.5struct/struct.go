package main

import "fmt"

type Member struct {
	id   string
	name string
	age  int
}

type Coordinate struct {
	x int
	y int
}

func main() {
	//構造耐を保存するスライスを作成する
	var members = []Member{}
	// でーたを作成してスライスを保存する
	members = append(members, Member{"A010", "ポチ", 17})
	members = append(members, Member{"A021", "犬太", 16})
	members = append(members, Member{"A023", "Sally", 21})

	//構造体のデータを作成して
	mem := Member{"C123", "花丘", 58}
	members = append(members, mem) //スライスに追加する

	fmt.Println(members)

	//構造体のデーターを作成する
	var pos = Coordinate{}
	pos.x = 123
	pos.y = 234

	fmt.Printf("x = %d y = %d", pos.x, pos.y)

}
