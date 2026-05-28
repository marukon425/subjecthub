# 1から100までの整数を合計して結果を表示
num = 1
sum = 0

while num <= 100:
    sum += num
    num += 1

print("合計：", sum, sep="")