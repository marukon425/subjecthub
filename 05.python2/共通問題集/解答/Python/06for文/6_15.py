# 整数を10回入力させ合計値を表示する
sum = 0

for i in range(1, 11):
    sum += int(input(str(i) + "回目の入力："))
    
# 合計値を表示
print("合計：", sum, sep="")
