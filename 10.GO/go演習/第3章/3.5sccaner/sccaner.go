// scanner.go
package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var name string
	fmt.Printf("名前を入力してください:")
	scanner := bufio.NewScanner(os.Stdin)

	scanner.Scan()
	name = scanner.Text()

	fmt.Printf("nameは=%s¥n", name)
}
