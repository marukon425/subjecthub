package main

import (
	"fmt"
	"html"
	"math/big"
	"net/http"
)

type Server struct{}

func (Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	left := r.FormValue("left")
	right := r.FormValue("right")
	naka := r.FormValue("naka")
	op := r.FormValue("op")

	leftInt := &big.Int{}
	rightInt := &big.Int{}
	nakaInt := &big.Int{}
	_, leftOK := leftInt.SetString(left, 10)
	_, rightOK := rightInt.SetString(right, 10)
	_, nakaOK := nakaInt.SetString(naka, 10)

	var result string
	if leftOK && rightOK && nakaOK {
		resultInt := &big.Int{}
		switch op {
		case "add":
			resultInt.Add(leftInt, nakaInt)
			resultInt.Add(resultInt, rightInt)
		case "sub":
			resultInt.Sub(leftInt, nakaInt)
			resultInt.Sub(resultInt, rightInt)
		case "multi":
			resultInt.Mul(leftInt, nakaInt)
			resultInt.Mul(resultInt, rightInt)
		case "div":
			resultInt.Div(leftInt, nakaInt)
			resultInt.Div(resultInt, rightInt)
		}
		result = resultInt.String()
	}

	h := `
<html><head><title>電卓アプリ</title></head><body>
  <form action="/" method="post">
    左項目：<input type="text" name="left"><br>
    中項目：<input type="text" name="naka"><br>
    右項目：<input type="text" name="right"><br>
    演算子：
    <input type="radio" name="op" value="add" checked> +
    <input type="radio" name="op" value="sub"> -
    <input type="radio" name="op" value="multi"> ×
    <input type="radio" name="op" value="div"> ÷
    <br><input type="submit" name="送信"><br>

    [フォームの入力値]<br>
    左項目：` + html.EscapeString(left) + `<br>
    中項目：` + html.EscapeString(naka) + `<br>
    右項目：` + html.EscapeString(right) + `<br>
    演算子：` + html.EscapeString(op) + `<hr>
    演算結果：` + html.EscapeString(result) + `
  </form>
</body></html>
`

	fmt.Fprint(w, h)
}

func main() {
	http.ListenAndServe(":4000", Server{})
}
