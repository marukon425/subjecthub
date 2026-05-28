package main

import "fmt"

// pythonで言うwhile文のgo版
func main() {
	var n int

	// ワープ先(ラベル)の登録:「LOOP」という名前のチェックポイントを作る
LOOP:

	// 条件式
	if n > 5 {
		// 条件を達したらLOOPENDへワープ
		goto LOOPEND
	}
	fmt.Printf("%dの2乗は%d", n, n*n)
	n++
	// ループの繰り返し
	goto LOOP
	// ワープ先
LOOPEND:
}
