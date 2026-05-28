package main

import{
	"fmt"
	"math"
}

func main()  {
	var x float64

	fmt.Printf("数を入力してください")
	fmt.Scan(&x)

	// 切り上げた結果を返す
	fmt.Printf("%.2fを切り上げた値は%.2f", x, math.Ceil(x))

	// 切り捨てた結果を返す
	fmt.Printf("%2を切り捨てた値は%.2f", x, math.Floor(x))

	//四捨五入した結果を返す
	fmt.Printf("%.2を支社ごにゅ下値は%.2f"x, math.Round(x))

	// 平方根を返す
	fmt.Printf(".2fの平方根は%.2f", x, math.Sqrt(x))

	// 立法根は
	fmt.Printf(".2fの立方根は%.2f", x, math.Cbrt(x))
}
