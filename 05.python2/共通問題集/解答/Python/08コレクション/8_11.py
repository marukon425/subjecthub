# 乱数を10個リストに格納してくじ引き結果を表示
import random

# 1等・2等・3等の数字のリストを作成
first_array = [0, 99]
second_array = [11, 22, 33, 44, 55, 66, 77, 88]
third_array = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95]

# 乱数を格納するリスト
array = []

# 乱数を10個発生させ格納
for _ in range(10):
    array.append(random.randint(0, 99))

# リストの全要素の1等・2等・3等・ハズレを表示
for i in array:
    if i in first_array:
        print(i, "を引きました。1等賞です！")
    elif i in second_array:
        print(i, "を引きました。2等賞です。")
    elif i in third_array:
        print(i, "を引きました。3等賞です。")
    else:
        print(i, "を引きました。残念ながらハズレです。")
