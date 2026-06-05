package main

import (
	"fmt"
	"os/exec"
)

// メモ帳が自動で開くプログラム

func main() {
	cmd := exec.Command("notepad", "sample.dat")

	err := cmd.Start()
	if err != nil {
		fmt.Println(err)
	}

	cmd.Wait() //終了を待つ
}
