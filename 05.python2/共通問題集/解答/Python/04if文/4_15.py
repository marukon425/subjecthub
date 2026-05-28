# 同値または最大値判定
print("整数値を3つ入力してください")
val1 = int(input("1つ目の整数値："))
val2 = int(input("2つ目の整数値："))
val3 = int(input("3つ目の整数値："))

# 同値の場合は「同じ値です」と表示し、それ以外の場合は最大値を判定し表示する
if val1 == val2 == val3 :
    print("同じ値です")
else :
    print("最大の値は", max(val1, val2, val3), "です")
