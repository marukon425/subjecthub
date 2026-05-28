// addargs.go
package main

import (
	"fmt"
	"os"
	"strconv"
)

func main() {
	if len(os.Args) < 3 {
		fmt.Println("引数を2個指定してください。")
		os.Exit(1)
	}

	var x, y int
	x, _ = strconv.Atoi(os.Args[1])
	y, _ = strconv.Atoi(os.Args[2])
	fmt.Printf("%d + %d = %d\n", x, y, x+y)
}
