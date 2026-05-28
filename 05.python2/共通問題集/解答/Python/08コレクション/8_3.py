# 入力された整数を偶数値のリストと奇数値のリストにそれぞれ格納して表示

# 偶数値リスト
even_array = []
# 奇数値リスト
odd_array = []

for i in range(10):
    num = int(input(str(i+1) + "件目：整数を入力 = "))

    # 偶数と奇数の判定
    if num % 2 == 0:
        # 偶数値リストに追加
        even_array.append(num)
    else:
        # 奇数値リストに追加
        odd_array.append(num)

# 偶数値リストの内容を表示
print("偶数値リスト =", even_array)

# 奇数値リストの内容を表示
print("奇数値リスト =", odd_array)
