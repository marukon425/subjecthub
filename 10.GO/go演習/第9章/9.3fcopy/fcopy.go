package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	// 🖐️ 引数の数をチェック（プログラム名、コピー元、コピー先の合計3つが必要）
	if len(os.Args) < 3 {
		fmt.Println("引数を２個指定してください。")
		os.Exit(1)
	}

	// コピー元のファイルを開く（読み込み専用）
	ifile, ierr := os.Open(os.Args[1])
	if ierr != nil {
		// 【修正1】fmt.Errorf から、画面にエラーを表示する fmt.Printf に修正
		fmt.Printf("%sを開けません。\n", os.Args[1])
		os.Exit(1)
	}
	defer ifile.Close() // 終わったら確実に閉じる

	// コピー先のファイルを新規作成する（書き込み用）
	ofile, oerr := os.Create(os.Args[2])
	if oerr != nil {
		// 【修正2】fmt.Errorf から、画面にエラーを表示する fmt.Printf に修正
		fmt.Printf("%sを開けません。\n", os.Args[2])
		os.Exit(1)
	}
	defer ofile.Close() // 終わったら確実に閉じる

	// 高速化のためにバッファー（一時的なメモリ置き場）を作る
	r := bufio.NewReader(ifile)
	w := bufio.NewWriter(ofile)

	// 【無限ループ】ファイルの中身を1バイトずつ最後までコピーする
	for {
		// 1バイト（1文字分）を読み込む
		c, err := r.ReadByte()
		if err != nil {
			// ファイルの最後まで読み切るとエラー（EOF）になるのでループを抜ける
			break
		}

		// 【修正3】インデントを綺麗に整え、1バイト書き込む
		oerr := w.WriteByte(c)
		if oerr != nil {
			fmt.Println(oerr)
			break
		}
	}

	// バッファーに溜まっているデータを、一気にファイルへ書き出す（超重要！）
	err := w.Flush()
	if err != nil {
		// 【修正4】古い変数「oerr」になっていたのを、直前の「err」に修正
		fmt.Println(err)
	}
}

// 実行方法:
// go build fcopy.go   → 実行ファイルを作成
// ./fcopy コピー元ファイル名 コピー先ファイル名
// 例: ./fcopy a.jpg b.jpg
// ※画像・テキストなど拡張子は何でもOK
