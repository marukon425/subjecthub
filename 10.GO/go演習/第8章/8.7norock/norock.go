package main

import (
	"fmt"
	"sync"
	"time"
)

// 共有で使う道具(グローバル変数)の準備
var wg sync.WaitGroup // 二人の作業が「両方終わるのを待つ」ためのタイマー
var a int             //みんなで同時に書き換える変数 初期値は10

// A君：数字を増やすかかり(１０回実行)
func jobplus() {
	defer wg.Done() // 10回のループが全部終わったら「終わったよと報告する」
	for i := 0; i < 10; i++ {
		t := a // 足す前の「a」の値を一時的にメモ

		// 1. 今の「a」の値を読みこんで、1を足して保存する
		// ☆値がないので、B君が書き換えてる最中にも勝手に触ってしっまう!
		a = a + 1

		// ちょこっと休憩
		time.Sleep(10 * time.Millisecond)
		//
		fmt.Printf("plus %d->%d\n", t, a)
	}
}

// B君：数字を減らす係(合計10回実行される状態)
func jobminus() {
	defer wg.Done()
	for i := 0; i < 10; i++ {
		t := a
		a = a - 1
		time.Sleep(11 * time.Millisecond)
		fmt.Printf("minus %d->%d\n", t, a)
	}
}

func main() {
	a = 10 // スタートの数字は10

	wg.Add(2) // 「二人の作業(jobpulusとjobminus)を待ちます」と設定

	// ※注意：Go言語の文法では「」
	go jobplus()  // Aくん、作業スタート！(バックグラウンドで並列処理)
	go jobminus() // Bくん、作業スタート！(バックグラウンドで並列処理)

	wg.Wait()
}
