package main

import "fmt"

func main() {
	var n int

	fmt.Printf("整数を入力してください")
	fmt.Scan(&n)

	// switch文
	switch n % 2 { // nを2で割った余り
	// ○○だった場合
	case 0:
		fmt.Printf("%dは偶数です", n)
	case 1:
		fmt.Printf("%dは奇数です", n)
	}

	switch n % 3 {
	case 0:
		fmt.Printf("%dは3の倍数です", n)
	default: // ← 何も当てはまらなかった場合
		fmt.Printf("%dは3の倍数ではありません", n)
	}

	switch n < 0 {
	case n < 0:
		fmt.Printf("%dは負の数です", n)
	case n > 0:
		fmt.Printf("%dは負の数です", n)
	default:
		fmt.Printf("%dはゼロです", n)
	}

	// こんな書き方もできる
	// fallthrough: 条件式に当てはまるもの全部に処理が実行される
	//    ↓条件式を書かない場合はfallthroughを末尾に着ける
	switch {
	case n == 0:
		fmt.Printf("%dはゼロです", n)
		fallthrough
	case n > 0:
		fmt.Printf("%dはふの整数ではない数です", n)
		fallthrough
	default:
		fmt.Printf("%dは整数です", n)
	}
}
