package main

import "fmt"

func main() {
	// スライスのベースとは言葉る配列を作る
	var a = [...]int{1, 3, 5, 7, 9}
	fmt.Printf("type(a)=%T", a)

	//スライスを作る
	var s = a[0:4]
	fmt.Printf("type=%T", s)

	//スライスの各要素を出力する
	for i, v := range s {
		fmt.Printf("s[%d]=%d", i, v)
	}

	s[1] = 0       //2番目の要素の値を変更する
	s[3] = 0       //4番目の要素の値を変更する
	fmt.Println(s) //スライス全体を出力する

	// make(でスライスを作る)
	var b = make([]int, 5, 20)

	b[1] = 18
	b[3] = 38
	fmt.Println(b) // スライス全体を出力する

	b = append(b, 88) // 要素を出力する
	fmt.Println(b)

	// make()スライス全体を追加する
	var d = make([]int, 5, 20)
	copy(d, s) //スライスをコピーする

	fmt.Println(d) // スライスを出力する

}
