# 2つのリストの要素同士を足し算した結果を表示する

# 整数値リスト
list_a = [10, 20, 30, 40, 50]
list_b = [22, 33, 44, 55, 66]
# 足し算した結果リスト
res_list = []

# 入力された整数値をリストに格納
for i in range(0, len(list_a)):
    res_list.append(list_a[i] + list_b[i])

# リストの全要素を表示
print("list_a =", list_a)
print("list_b =", list_b)
print("list_a + list_b =", res_list)
