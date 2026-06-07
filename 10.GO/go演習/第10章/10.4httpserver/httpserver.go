// httpserver.go
package main

import (
	"fmt"
	"log"
	"net/http"
)

func main() {
	fmt.Println("サーバースタート ([Ctrl]+[C]で終了) ")
	// リクエスト処理関数を設定する
	http.HandleFunc("/", handler)
	// クライアントに耳を傾けサービスを開始する
	err := http.ListenAndServe("localhost:8000", nil)
	if err != nil {
		log.Fatal(err)
	}
}

// リクエスト処理関数
func handler(w http.ResponseWriter, r *http.Request) {
	// クライアントに文字列を送る
	fmt.Fprintf(w, "<html>\n<body>\n")
	fmt.Fprintf(w, "<h1>httpserverへようこそ</h1>\n")
	fmt.Fprintf(w, "<p>サーバーは: %q</p>\n", r.Host)
	fmt.Fprintf(w, "<p>リモートアドレスは: %q</p>\n", r.RemoteAddr)
	fmt.Fprintf(w, "<img src='IMG_7138.PNG' alt=''>")
	fmt.Fprintf(w, "</body>\n</html>\n")
	if err := r.ParseForm(); err != nil {
		log.Print(err)
	}
}
