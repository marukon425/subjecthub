package main

import (
	"fmt"
	"strings"
	"time"
)

// 構造体(TextOp)の定義
type TextOp struct {
	Text string
}

// process メソッドの定義
// 指定された 処理種別 op の種類により、各種処理を実行し、実行結果を表示
func (t *TextOp) process(op string) {
	fmt.Println("ゴルーチン開始")
	switch op {
	case "len":
		fmt.Println("\"Hello\" の長さは", len(t.Text))
	case "toUpper":
		fmt.Println("\"Hello\" を大文字にすると", "\""+strings.ToUpper(t.Text)+"\"")
	case "toLower":
		fmt.Println("\"Hello\" を小文字にすると", "\""+strings.ToLower(t.Text)+"\"")
	}
	fmt.Println("ゴルーチン終了")
}

func main() {
	fmt.Println("main関数開始")

	// 穴埋め(1)：構造体の変数宣言
	var textOp TextOp

	// 操作対象の文字列を設定
	textOp.Text = "Hello"

	// go ○○でゴルーチンを実行する
	go textOp.process("toUpper")
	go textOp.process("toLower")
	go textOp.process("len")

	time.Sleep(time.Second)
	fmt.Println("main関数終了")
}

// ゴルーチンの実行のやり方は 「go 〇〇」で実行するだけ!

// ゴルーチンが完了する前にmainが終了するのを防ぐため
// （mainが終わるとゴルーチンも強制終了される）
