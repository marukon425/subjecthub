package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strings"
)

func main() {
	if len(os.Args) < 2 {
		fmt.Println("引数にURLを指定してください。")
		os.Exit(1)
	}

	url := os.Args[1]
	if !strings.HasPrefix(url, "http://") && !strings.HasPrefix(url, "https://") {
		url = "http://" + url
	}

	// HTTP GET
	resp, err := http.Get(url)
	if err != nil {
		fmt.Fprintf(os.Stderr, "http.Get()でエラー発生(%v)\n", err)
		os.Exit(1)
	}
	defer resp.Body.Close()

	// ボディ読み込み
	src, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Fprintf(os.Stderr, "ReadAll()でエラー発生(%v)\n", err)
		os.Exit(1)
	}

	fmt.Printf("%s", src)
}

// 実行の仕方 go run main.go https://example.com
