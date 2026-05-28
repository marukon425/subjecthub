// gofunc.go
package main

import (
	"fmt"
	"sync"
	"time"
)

func main() {
	// 出席簿(カウンター)を用意する
	var wg sync.WaitGroup

	// "ABC"から１文字ずつ取り出してループ
	for _, c := range "ABC" {
		ch := c
		fmt.Printf("%c start\n", c)

		go func() {
			wg.Add(1)
			for i := 0; i < 10; i++ {
				time.Sleep(10 * time.Millisecond)
				fmt.Printf("%c", ch)
			}
			defer wg.Done()
		}()
	}

	wg.Wait()
	fmt.Printf("\n終了\n")
}
