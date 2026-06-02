// wrpoints.go
/*
このプログラムは、「グラフ上の点（座標）のデータを、ファイルに保存したり、ファイルから読み込んだりする仕組み」
プログラムが終了してもデータが消えないように、「データをハードディスク（ファイル）に書き残し、次回また使えるようにすること」が目的
⓵データを作る
(5, 5) や (7, 8) といった、X座標とY座標を持つ「5つの点（Point）」をプログラムの中で作ります。
⓶ファイルに保存する（Save関数）
作った5つの点のデータを、points.data というテキストファイルに書き込んで保存します。
ファイルの中身は、ノートにメモするように 5 5、7 8 と1行ずつ数字が並んだ状態になります。
⓷ファイルから読み込む（Load関数）
今度は、さっき保存した points.data ファイルをプログラムで開き、中身の数字を1行ずつ読み込んで、
再びプログラムの中で使えるデータ（配列）に戻します。
⓸確認する
最後に、「ファイルから無事に読み込めたデータ」を画面に表示して、正しく保存・復元ができたかを確かめています。
*/
package main

import (
	"fmt"
	"log"
	"os"
)

// Point 型の定義
type Point struct {
	x, y int
}

const fname = "points.data"

// Load - 点の情報を読み込むメソッド

func Load() []Point {
	var points = []Point{}
	// ファイルを開く
	file, err := os.OpenFile(fname, os.O_RDONLY, 0666) // 【解説】os.O_RDONLY は「読み取り専用」でファイルを開くモードだよ！
	if err != nil {
		log.Fatal(err)
	}

	// ファイルから読み込む
	var x, y int
	for {
		// 【解説】fmt.Fscanf は、指定したファイル（file）から形式に合わせてデータを1行ずつ読み込むよ。
		n, err := fmt.Fscanf(file, "%d %d\n", &x, &y)
		// 【解説】n には正しく読み込めたデータの数が入るよ。データの終わり（EOF）やエラーの時はループを抜ける（break）よ。
		if n == 0 || err != nil {
			break
		} else {
			// 【解説】append はスライス（可変長配列）の末尾に、新しく作った Point 構造体を追加する関数だよ！
			points = append(points, Point{x, y})
		}
	}

	// ファイルを閉じる
	file.Close() // 【解説】開いたファイルは、使い終わったら必ず Close() で閉じるのが鉄則だよ！
	return points
}

// Save - 点の情報を保存するメソッド
func Save(points []Point) int {
	// 【解説】os.O_RDWR（読み書き用）と os.O_CREATE（ファイルが無ければ新しく作る）を「|」で合体させて指定しているよ！
	file, err := os.OpenFile(fname, os.O_RDWR|os.O_CREATE, 0666)
	if err != nil {
		log.Fatal(err)
	}

	// ファイルに書き込む
	for _, p := range points {
		// 【解説】fmt.Fprintf は、いつも画面に出力する fmt.Printf の「ファイル書き込み版」だよ！
		fmt.Fprintf(file, "%d %d\n", p.x, p.y)
	}
	// ファイルを閉じる
	file.Close()
	return len(points) // 書き込んだ点の数を返す
}

func main() {
	var points = []Point{}
	// 5このデータを作る
	points = append(points, Point{5, 5})
	points = append(points, Point{7, 8})
	points = append(points, Point{4, 3})
	points = append(points, Point{7, 4})
	points = append(points, Point{9, 5})

	// データを表示する
	fmt.Println("書き込むデータ")
	for i, p := range points {
		// 【解説】i は 0 から始まるインデックスだから、画面上で「1番目」から始めたいときは i + 1 にするよ！
		fmt.Printf("point[%d] = (%d, %d)\n", i+1, p.x, p.y)
	}
	// データを保存する
	Save(points)

	// データを保存する
	// 【解説】上で保存したばかりの "points.data" ファイルを開いて、中身を data という変数に読み込んでいるよ。
	data := Load()

	// 読み込んだデータを表示する
	fmt.Println("読み込んだデータ")
	for i, p := range data {
		fmt.Printf("point[%d] = (%d, %d)\n", i+1, p.x, p.y)
	}
}

/*
ゲームのセーブ機能や、スマホアプリの設定の保存、
実験データの記録など、実用的なシステムはすべて
この「ファイルへの読み書き」を行っています。
その最も基礎となる書き方を、このプログラムで練習しています。
*/
