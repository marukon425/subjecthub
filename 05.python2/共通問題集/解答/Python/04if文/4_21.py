import random

num1 = random.randint(0,9)
num2 = random.randint(0,9)
num3 = random.randint(0,9)
num4 = random.randint(0,9)

# 計算式の表示
print(num1, "+", num2, "×", num3, "-", num4, "=")
# 計算実行
result = num1 + num2 * num3 - num4

# 計算結果の予想を入力させる
input_result = int(input("計算結果は？："))

# 計算結果の判定
if result == input_result:
    print("正解です！")
else:
    print("不正解です。正解は", result, "です。", sep="")
