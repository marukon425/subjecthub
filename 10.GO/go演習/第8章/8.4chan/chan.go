package main

import (
	"fmt"
	"time"
)

func main() {
	// チャンネルを作る
	done := make(chan bool)

	// ゴルーチンで(裏側)"*"を出力する
	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(10 * time.Millisecond)
			fmt.Printf("*")
		}
		// 【合図を送る】自分の仕事が10回終わったので、倍部に「true」を投げ入れる
		// メイン(表側)が受け取ってくれるまで、ここで一旦ストップします
		done <- true // 終わったらtrueを送る
	}()

	// メインルーチンで(表側)"/"を出力する
	for i := 0; i < 10; i++ {
		time.Sleep(10 * time.Millisecond)
		fmt.Printf("/")
	}
	// 【合図を待つ】パイプからデータ(true)が流れてくるのを、ここでじっと待つ
	// データが届くまでは、絶対に次の行(終了)へ進まないという協力なブレーキになります
	<-done // trueが送られるのを待って受け取る

	fmt.Printf("\n終了\n")
}
