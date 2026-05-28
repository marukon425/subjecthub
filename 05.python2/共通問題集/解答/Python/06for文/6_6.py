# 合計値格納変数の初期化
sum = 0

# 入力された値を数値に変換して格納
start = int(input("開始数："))
end = int(input("終了数："))

# 開始数から終了数まで数を加算
for num in range(start, end+1):
    sum += num

# 結果を表示
print("合　計：", sum, sep="")
