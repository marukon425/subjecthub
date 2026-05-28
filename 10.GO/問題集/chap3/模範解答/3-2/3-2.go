// 3-2.go
/** 

  キーボードから二つの整数値を入力し 

  四則演算を行い結果を表示 

*/ 
package main 

import"fmt" 

func main() { 

// 変数 data1, data2 を宣言（型 int32） 

var data1, data2 int32

// 変数 addAns, subAns, mulAns, modAns を宣言（型 int32） 

var addAns, subAns, mulAns, modAns int32

// 変数 divAns を宣言（型 float32） 

var divAns float32

// 入力促進 
fmt.Print("data1 = ")
// キーボードから1つ目の整数値を入力 
fmt.Scan(&data1)
// 入力促進 
fmt.Print("data2 = ")
// キーボードから２つ目の整数値を入力 
fmt.Scan(&data2)

// 四則演算 
// 加算 
addAns = data1 + data2

// 減算 
subAns = data1 - data2

// 乗算 
mulAns = data1 * data2
// 除算
divAns = float32(data1) / float32(data2)
// 剰余 
modAns = data1 % data2 

// 四則演算結果を表示 
// 加算 
fmt.Printf("%d + %d = %d\n", data1, data2, addAns)

// 減算 
fmt.Printf("%d - %d = %d\n", data1, data2, subAns)

// 乗算 
fmt.Printf("%d * %d = %d\n", data1, data2, mulAns)
// 除算
fmt.Printf("%d / %d = %.6f\n", data1, data2, divAns)
// 剰余 
fmt.Printf("%d %% %d = %d\n", data1, data2, modAns)
fmt.Println("")
} 
