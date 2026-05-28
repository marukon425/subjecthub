/**
キーボードからチャンネル番号を入力し
対応するテレビ局名を表示する
*/
package main

import "fmt"

func main() {
	// 変数 channelNumber（チャンネル番号）の宣言（型　unit32）
	var channelNumber uint32
	// 変数 tvStationName（テレビ局名）の宣言（型 string）
	var tvStationName string

	// キーボードからチャンネル番号を入力
	// 入力促進
	fmt.Print("チャンネル番号入力 = ")
	// キーボードからチャンネル番号を入力し、変数 channelNumber に保存
	fmt.Scan(&channelNumber)

	// チャンネル番号に対応するテレビ局名を選択
	switch channelNumber {
	case 1:
		tvStationName = "NHK総合"
	case 3:
		tvStationName = "NHK教育"
	case 4:
		tvStationName = "日本テレビ"
	case 6:
		tvStationName = "TBS"
	case 8:
		tvStationName = "フジテレビ"
	case 10:
		tvStationName = "朝日テレビ"
	case 12:
		tvStationName = "東京12チャンネル"
	default:
		tvStationName = "ありません"
	}

	// チャンネル番号に対応するテレビ局名を表示
	fmt.Printf("チャンネル番号 %d に対応するテレビ局名は、%s\n",
		channelNumber, tvStationName)
}
