# 合計値格納変数の初期化
ans = 0

# 入力された値を数値に変換して格納
start = int(input("開始数："))
end = int(input("終了数："))

# 開始数から終了数まで数をリストにして合計
ans = sum([num for num in range(start, end+1)])

# 結果を表示
print("合　計：", ans, sep="")