# 乱数を10個リストに格納して合計値と最大値とリスト内の全要素を表示
import random

# 乱数を格納するリスト
array = []

# 乱数を10個発生させ格納
for _ in range(10):
    array.append(random.randint(0, 99))

# 合計値を表示
print("合計値は", sum(array), "です。", sep="")

# 最大値を表示
print("最大値は", max(array), "です。", sep="")

# リストの全要素を表示
index = 0
for i in array:
    print("リスト[", index ,"]：", i, sep="")
    index += 1
