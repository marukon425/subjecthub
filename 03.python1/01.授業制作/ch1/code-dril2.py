'''
数値１を入力
数値２を入力
〇　+　〇　＝　〇
数値３を入力
数値４を入力
〇　×　〇　＝　〇
'''

# 変数(num1)(num2)に整数型(int)に変換しながらデータを入力 → 計算結果を表示
num1 = int(input("数値１を入力"))
num2 = int(input("数値2を入力"))
print(num1, "+", num2, "=", num1 + num2 )


num3 = int(input("数値3を入力"))
num4 = int(input("数値4を入力"))
print(num3, "×", num4, "=", num3 * num4)