package main

import (
	"fmt"
	"html"
	"math/big"
	"net/http"
	"strings"
)

type Server struct{}

func calcComma(nums []*big.Int, op string) string {
	if len(nums) == 0 {
		return ""
	}
	result := new(big.Int).Set(nums[0])
	for _, n := range nums[1:] {
		switch op {
		case "+":
			result.Add(result, n)
		case "-":
			result.Sub(result, n)
		case "×":
			result.Mul(result, n)
		case "÷":
			if n.Sign() == 0 {
				return "ゼロ除算エラー"
			}
			result.Div(result, n)
		}
	}
	return result.String()
}

func (Server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	left := r.FormValue("left")
	right := r.FormValue("right")
	naka := r.FormValue("naka")
	op := r.FormValue("op")
	listOp := r.FormValue("list-select")
	listNums := r.FormValue("list")

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
	} else {
		result = "数値を入力してください!!!"
	}

	var listResult string
	if listNums != "" {
		parts := strings.Split(listNums, ",")
		nums := make([]*big.Int, 0, len(parts))
		allOK := true
		for _, p := range parts {
			n := &big.Int{}
			_, ok := n.SetString(strings.TrimSpace(p), 10)
			if !ok {
				allOK = false
				break
			}
			nums = append(nums, n)
		}
		if allOK {
			listResult = calcComma(nums, listOp)
		} else {
			listResult = "数値を入力してください!!!"
		}
	}

	options := ""
	for i := 0; i < 1000; i++ {
		options += fmt.Sprintf(`<option value="%d">%d</option>`, i, i)
	}
	h := `
<html><head><title>電卓アプリ</title></head><body>
  <form action="/" method="post">
    左項目：<input type="text" name="left" value=0><br>
	中項目：<select name="naka" id="naka">
		` + options + `
	</select><br>
    右項目：<input type="text" name="right" value=0><br>
    演算子：
    <input type="radio" name="op" value="add" checked> +
    <input type="radio" name="op" value="sub"> -
    <input type="radio" name="op" value="multi"> ×
    <input type="radio" name="op" value="div"> ÷
    <br><input type="submit" name="送信"><br>
	</form>
	カンマ区切りの計算(例 1,2,3,4,5)<br>
	<select name="list-select" id="select">
	<option value="+">+</option>
	<option value="-">-</option>
	<option value="×">×</option>
	<option value="÷">÷</option>
	</select>
	<input type="text" name="list" value="` + html.EscapeString(listNums) + `">

	-------------------------------------------------------------------------------------------------------------------------<br>

    [フォームの入力値]<br>
    左項目：` + html.EscapeString(left) + `<br>
    中項目：` + html.EscapeString(naka) + `<br>
    右項目：` + html.EscapeString(right) + `<br>
    演算子：` + html.EscapeString(op) + `<hr>
    演算結果：` + html.EscapeString(result) + `<br>
	カンマ区切り演算結果：` + html.EscapeString(listResult) + `
</body></html>
`

	fmt.Fprint(w, h)
}

func main() {
	http.ListenAndServe(":4000", Server{})
}
