package main

import (
	"bufio"
	"fmt"
	"log"
	"net"
	"strings"
	"time"
)

// 接続を処理する
func handleConn(c net.Conn) {
	input := bufio.NewScanner(c)
	for input.Scan() {
		msg := input.Text()
		go func() {
			if strings.ToLower(msg) == "hello" {
				if time.Now().Hour() < 12 {
					fmt.Fprintln(c, "[おはよう]")
				} else {
					fmt.Fprintln(c, "[おはよう]")
				}
			} else {
				fmt.Fprintln(c, "[", strings.ToUpper(msg), "]")
			}
			time.Sleep(500 * time.Millisecond)
		}()
	}
	c.Close()
}

func main() {
	fmt.Println("サーバースタート")

	// 接続してクライアントに耳を傾ける
	l, err := net.Listen("tcp", "localhost:8000")
	if err != nil {
		log.Fatal(err)
	}

	// 個々の接続を処理する
	for {
		conn, err := l.Accept()
		if err != nil {
			log.Print(err)
			continue
		}
		go handleConn(conn)
	}
}
