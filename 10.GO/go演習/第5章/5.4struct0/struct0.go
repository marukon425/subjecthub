package main

import "fmt"

// Member - メンバーの構造体
type Member struct {
	ID   string
	Name string
	Age  int
}

func main() {
	var mp = new(Member)
	// *mpは「mpという住所にある部屋そのもの」という意味
	*mp = Member{"C123", "花丘", 58}
	// 部屋の中身(データを画面に出力する)
	fmt.Println(*mp)

	var mp1 = new(Member)

	mp1.ID = "D123"
	mp1.Name = "吉野"
	mp1.Age = 27

	fmt.Println(*mp1)
}
