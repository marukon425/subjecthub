package main

import (
	"fmt"
	"html"
	"math/big"
	"net/http"
	"strings"
)

type Server struct{}

// 普通の計算（左・中・右の3項）
func calcNormal(left, naka, right *big.Int, op string) string {
	result := new(big.Int)
	switch op {
	case "add":
		result.Add(left, naka)
		result.Add(result, right)
	case "sub":
		result.Sub(left, naka)
		result.Sub(result, right)
	case "multi":
		result.Mul(left, naka)
		result.Mul(result, right)
	case "div":
		if naka.Sign() == 0 || right.Sign() == 0 {
			return "ゼロ除算エラー"
		}
		result.Div(left, naka)
		result.Div(result, right)
	default:
		return "演算子を選択してください"
	}
	return result.String()
}

// リストの要素同士の四則演算（カンマ区切り）
func calcList(nums []*big.Int, op string) string {
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
	// --- 普通の計算フォームの値 ---
	left := r.FormValue("left")
	right := r.FormValue("right")
	naka := r.FormValue("naka")
	op := r.FormValue("op")

	// --- リスト計算フォームの値 ---
	listOp := r.FormValue("list-select")
	listNums := r.FormValue("list")

	// 普通の計算処理
	var result string
	leftInt := &big.Int{}
	rightInt := &big.Int{}
	nakaInt := &big.Int{}
	_, leftOK := leftInt.SetString(left, 10)
	_, rightOK := rightInt.SetString(right, 10)
	_, nakaOK := nakaInt.SetString(naka, 10)

	if left != "" || right != "" || naka != "" || op != "" {
		if leftOK && rightOK && nakaOK {
			result = calcNormal(leftInt, nakaInt, rightInt, op)
		} else {
			result = "数値を入力してください!!!"
		}
	}

	// リスト計算処理
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
			listResult = calcList(nums, listOp)
		} else {
			listResult = "数値を入力してください!!!"
		}
	}

	// 中項目セレクトボックスの選択肢（0〜999）
	options := ""
	for i := 0; i < 1000; i++ {
		options += fmt.Sprintf(`<option value="%d">%d</option>`, i, i)
	}

	h := `
<html><head><title>電卓アプリ</title></head><body>

<h2>普通の計算</h2>
<form action="/" method="post">
  左項目：<input type="text" name="left" value="` + html.EscapeString(left) + `"><br>
  中項目：<select name="naka" id="naka">` + options + `</select><br>
  右項目：<input type="text" name="right" value="` + html.EscapeString(right) + `"><br>
  演算子：
  <input type="radio" name="op" value="add" checked> +
  <input type="radio" name="op" value="sub"> -
  <input type="radio" name="op" value="multi"> ×
  <input type="radio" name="op" value="div"> ÷
  <br>
  <input type="submit" value="計算する"><br>
</form>
<b>演算結果：` + html.EscapeString(result) + `</b>

<hr>

<h2>リストの要素同士の四則演算</h2>
<form action="/" method="post">
  数値をカンマ区切りで入力（例: 1,2,3,4,5）<br>
  <input type="text" name="list" value="` + html.EscapeString(listNums) + `" size="40"><br>
  演算子：
  <select name="list-select">
    <option value="+">+</option>
    <option value="-">-</option>
    <option value="×">×</option>
    <option value="÷">÷</option>
  </select><br>
  <input type="submit" value="計算する"><br>
</form>
<b>リスト演算結果：` + html.EscapeString(listResult) + `</b>

</body></html>
`

	fmt.Fprint(w, h)
}

func main() {
	http.ListenAndServe(":4000", Server{})
}
