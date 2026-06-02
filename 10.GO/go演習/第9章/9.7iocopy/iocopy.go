// iocopy.go
/*
このプログラムの目的は、「自分で作れるファイルコピー専用のコマンドラインツール（簡易版 cp コマンド）」
実行方法例　go run iocopy.go sample.txt backup.txt
このように動かすと、sample.txt の中身がそのまま backup.txt にコピーされます。

*/
package main

import (
	"fmt"
	"io"
	"os"
)

func main() {
	// 【解説】os.Args には、コマンドラインで入力した引数（プログラム名、コピー元、コピー先）が配列のように入るよ。
	// 【解説】引数が3個未満（＝ファイルを2つ指定していない）の場合は、使い方が違うのでエラーメッセージを出すよ。
	if len(os.Args) < 3 {
		fmt.Println("引数を２個指定してください。")
		os.Exit(1) // 【解説】プログラムをここで強制終了させるおまじないだよ。
	}

	// ファイルを開く
	// 【解説】os.Args[1]（1番目の引数）で指定された、コピー元のファイルを「読み込み専用」で開くよ。
	src, err := os.Open(os.Args[1])
	if err != nil {
		panic(err) // 【解説】ファイルが見つからないなどの深刻なエラーが起きたら、ここで処理をストップするよ。
	}
	// 【解説】defer をつけておくと、main関数が終わる直前に、自動でこのファイルを安全に閉じて（Close）くれるよ！便利！
	defer src.Close()

	// 【解説】os.Args[2]（2番目の引数）で指定された、コピー先のファイルを新しく作る（または上書きする）よ。
	dst, err := os.Create(os.Args[2])
	if err != nil {
		panic(err)
	}
	defer dst.Close()

	// ファイルをコピーする
	// 【解説】io.Copy は、コピー元（src）の中身を丸ごとコピー先（dst）へ一瞬で流し込んでくれる超強力な関数だよ！
	// 【解説】左側の「_（ブランク識別子）」は、今回は使わない「コピーしたバイト数」という戻り値を捨てるために使っているよ。
	_, err = io.Copy(dst, src)
	if err != nil {
		panic(err)
	}
}
