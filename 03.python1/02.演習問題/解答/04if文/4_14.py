# 同値または大きい値の判定
print("0～100までの整数値を2つ入力してください")
val1 = int(input("1つ目の値："))
val2 = int(input("2つ目の値："))

if val1 == val2 :
    print("同じ値です")
else :
    print("大きい方の値は" , val1 if val1 > val2 else val2, "です", sep="")
