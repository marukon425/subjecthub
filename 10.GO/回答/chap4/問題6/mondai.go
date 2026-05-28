package main

import "fmt"

func main() {
	var score int32
	var evaluation string
	fmt.Print("得点を入力¥n")
	fmt.Scan(&score)

	if score >= 80 {
		evaluation = "Sランク"
	} else if score >= 70 {
		evaluation = "Aランク"
	} else if score >= 50 {
		evaluation = "Cランク"
	} else if score >= 40 {
		evaluation = "Dランク"
	} else {
		evaluation = "不合格"
	}

	fmt.Printf("成績の評価は、%d です", evaluation)

}
