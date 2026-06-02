package main

import (
	"fmt"
	"time"
)

func main() {
	// チャンネルを作る
	ch1 := make(chan rune)
	ch2 := make(chan int)
	done := make(chan bool)

	// ゴルーチンで文字を送る
	go func() {
		s := "ABCDEF"
		for _, c := range s {
			time.Sleep((10 * time.Millisecond))
			fmt.Printf("ch1から送信：%c\n", c)
			ch1 <- c
		}
		done <- true //終わったらtrueを送る
	}()

	// ゴルーチンで数値を送る
	go func() {
		for i := 0; i < 8; i++ {
			time.Sleep(8 * time.Millisecond)
			fmt.Printf("ch2から送信：%d\n", i)
			ch2 <- i + 1
		}
		done <- true // 終わったらtrueを送る
	}()

	defer fmt.Println("終了")
	count := 0
	// メインルーチンで受け取ったデータを出力する
	for {
		select {
		case r := <-ch1:
			fmt.Printf("ch1から受信：%c\n", r)
		case n := <-ch2:
			fmt.Printf("ch2から受信：%d\n", n)
		case <-done: // trueが2個送られたら終了
			count++
			if count > 1 {
				return
			}
		}
	}
}
