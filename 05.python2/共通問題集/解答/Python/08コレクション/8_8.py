# 整数値を3つ入力させリストに格納後、最大値と最小値を表示する

# 整数値リスト
array = []

print("整数値を3つ入力してください。")

# 入力された整数値をリストに格納
for i in range(1, 4):
    array.append(int(input(str(i) + "つ目の整数値：")))

# 最大値を表示
print("最大値：", max(array), sep="")

# 最小値を表示
print("最小値：", min(array), sep="")
