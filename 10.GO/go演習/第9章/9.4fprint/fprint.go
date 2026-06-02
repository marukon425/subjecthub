// fprint.go
package main

import (
	"fmt"
	"io/ioutil" // 📄 ファイルを1行で一気に読み込める超便利パッケージ（現在は io に統合が進んでいます）
	"log"       // 🚨 エラーが起きた時に、時間を記録してプログラムを強制終了させる道具
	"os"
)

func main() {
	// 📄 使うファイルの名前を決める（バッククォート `` ` `` で囲むと特殊文字もそのまま扱える文字列になる）
	fname := `sample.dat`

	// 【配列の宣言】`[...]string` と書くことで、右側の要素数（5個）を自動で数えて固定長の配列を作ってくれる
	words := [...]string{"Dog", "Cat", "Pig", "Deer", "Raccoons"}

	// ─── ✨ 【前半戦】書式を指定してファイルへ書き込む ───

	// 【os.OpenFile構文】
	// os.O_RDWR（読み書き両用） | os.O_CREATE（無ければ新規作成） という条件を合体させてファイルを開く
	// 「0666」はLinuxなどで使われるファイルの権限（パーミッション）で、「誰でも読み書きOK」という意味
	file, err := os.OpenFile(fname, os.O_RDWR|os.O_CREATE, 0666)

	// 🛠️【タイポ修正箇所】err の中身が nil（空っぽ）「ではない（!=）」、つまりエラーの時の処理
	if err != nil {
		log.Fatal(err) // エラー内容を画面に出して、ここでプログラムを即座に強制終了（Exit）する
	}

	// 【for-range構文（超重要）】
	// 配列（words）の中身を先頭から1つずつ自動で取り出すループ
	// i には「0からのインデックス番号（0, 1, 2...）」、w には「文字データ（Dog, Cat...）」が自動で入る
	for i, w := range words {

		// 【fmt.Fprintf関数】
		// 画面ではなく「開いているファイル（file）」に向けて、文字の形を整えて（Format）直接書き込む構文
		// `%03d` は「数字を3桁で表示し、空いたスペースは0で埋める（001, 002など）」という意味の書式
		fmt.Fprintf(file, "%03d %s\n", i+1, w)
	}

	// 書き込み用のファイルを閉じて、保存を確定させる
	file.Close()

	// ─── 📖 【後半戦】 ioutil を使って1行で一気に読み込む ───

	// 【ioutil.ReadFile関数】
	// 「ファイルを開く ➔ 中身を全部メモリに吸い出す ➔ 自動でファイルを閉じる」をこれ1行で完結させる神機能！
	txt, rerr := ioutil.ReadFile(fname)
	if rerr != nil {
		log.Fatal(rerr)
	}

	// 画面に出力する。txtの中身はパソコン用の「数字の列（[]byte）」なので、
	// string(txt) と書いて人間の読める「文字列型」に変換（キャスト）して表示する
	fmt.Println(string(txt))
}
