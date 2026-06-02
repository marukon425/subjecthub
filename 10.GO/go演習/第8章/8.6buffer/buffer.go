package main

import (
	"fmt"
	"time"
)

func main() {
	// チャンネルを作る
	done := make(chan bool, 3)

	// ゴルーチンで"+"を出力する
	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(10 * time.Millisecond)
			fmt.Printf("+")
		}
		done <- true // 終わったらtrueを送る
	}()

	// ゴルーチンで"-"を出力する
	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(10 * time.Millisecond)
			fmt.Printf("-")
		}
		done <- true // 終わったらtrueを送る
	}()

	// ゴルーチンで"¥"を出力する
	go func() {
		for i := 0; i < 10; i++ {
			time.Sleep(10 * time.Millisecond)
			fmt.Printf("¥¥")
		}
		done <- true // 終わったらtrueを送る
	}()

	// メインルーチンで"/"を出力する
	for i := 0; i < 10; i++ {
		time.Sleep(10 * time.Millisecond)
		fmt.Printf("/")
		time.Sleep(5 * time.Millisecond)
	}

	for i := 0; i < 3; i++ {
		<-done //trueが送られるのを待って受け取る
	}

}
