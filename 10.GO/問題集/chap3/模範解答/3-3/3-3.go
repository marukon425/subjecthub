/**
キーボードから身長（ｃｍ単位）、体重（Kg単位）
を入力しBMI値と適正体重を求めて表示する
但し、BMI値は以下の計算を行う
	BMI = 体重kg／（身長m）2
	適正体重 = 22×（身長m）2
*/
package main

import "fmt"

func main() {
	// 変数 height, weight の宣言（型　float64）
	var height, weight float64

	// 身長（ｍ　単位）を入力
	// 入力促進
	fmt.Print("身長（ｃｍ単位）を入力 = ")
	// 身長（ｃｍ単位）を入力し、変数 height に保存
	fmt.Scan(&height)

	// 体重（ｋｇ単位）を入力
	// 入力促進
	fmt.Print("体重（ｋｇ単位）を入力 = ")
	// 体重（ｋｇ単位）を入力し、変数 weight に保存
	fmt.Scan(&weight)

	// 変数 height をcm換算し、変数 heightCM に代入
	heightCM := height / 100.0

	// BMI値を計算し、変数 bmi に代入
	bmi := weight / (heightCM * heightCM)
	// 適正体重を計算し、変数 sutableWeight に代入
	sutableWeight := 22 * (heightCM * heightCM)

	// BMI値を表示
	fmt.Printf("BMI = %f\n", bmi)
	// 適正体重を表示
	fmt.Printf("適正体重 = %f\n", sutableWeight)
}
