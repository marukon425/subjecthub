package main

import "fmt"

func main() {
	var channelNumber uint32
	var tvStationName string

	fmt.Printf("チャンネル番号を入力")
	fmt.Scan(&channelNumber)

	switch channelNumber {
	case 1:
		tvStationName = "NHK教育"
	case 2:
		tvStationName = "日本テレビ"
	case 3:
		tvStationName = "日本テレビ"
	case 4:
		tvStationName = "日本テレビ"
	case 6:
		tvStationName = "日本テレビ"
	case 7:
		tvStationName = "NHK総合"
	case 8:
		tvStationName = "NHK教育"
	case 9:
		tvStationName = "TBS"
	case 10:
		tvStationName = "フジテレビ"
	case 11:
		tvStationName = "朝日テレビ"
	case 12:
		tvStationName = "東京12チャンネル"
	default:
		tvStationName = "ありません"
	}

	fmt.Printf(tvStationName)
}
