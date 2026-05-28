// gosample.go
package main

import (
	"fmt"
	"sync" // 関数処理(タイミングを合わせる機能)を使うためのパッケージ
	"time"
)

// 複数の処理が「終わるのを待つ」ための、共通の「出席簿(カウンター)」を作る
var wg sync.WaitGroup

func printjob(s string) {
	// 関数の処理がすべて終わった(終了して帰る)時に、自動的に実行される命令
	// 出席簿のカウンターを-1にして、「自分の仕事が終わったよ」と報告する
	defer wg.Done()
	for i := 0; i < 10; i++ {
		time.Sleep(10 * time.Millisecond)
		fmt.Printf("%s", s)
	}
}

func main() {
	// 「これから3つの仕事を裏で動かすから、3つ終わるまで待ってね」と出席簿に登録
	wg.Add(3)

	fmt.Println("A start")
	go printjob("A") // 裏で起動(終わったらカウンターが+1される)

	fmt.Println("B start")
	go printjob("B")

	fmt.Println("C start")
	go printjob("C")

	wg.Wait()

	fmt.Printf("\n結果\n")
}
