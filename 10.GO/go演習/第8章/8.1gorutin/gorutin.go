// goroutine.go
package main

import (
	"fmt"
	"time"
)

// 指定された回数(10回)画面に出力する関数
func printjob(s string) {
	for i := 0; i < 10; i++ {
		// 10ミリ秒だけ処理を一時停止する
		time.Sleep(10 * time.Millisecond)
		//改行せずに文字を出力する
		fmt.Printf("%s", s)
	}
}

func main() {
	// Aのジョブを「バックグラウンド」で起動
	fmt.Println("A start")
	go printjob("A") // goをつけると、終了を待たずに次の処理へ移行

	// Bのジョブも「バックグラウンド」で起動
	fmt.Println("B start")
	go printjob("B")

	// Cのジョブを「その場」で起動
	fmt.Println("C start")
	go printjob("C")

	// 全ての処理が混ざり合って終わるのを1秒間待つ
	time.Sleep(1 * time.Second)

	fmt.Printf("\n終了\n")
}
