# 合計値保持変数の初期化
sum = 0

# 1から100までの合計値を求める
for i in range(1, 101):
    sum += i

print("合計値は", sum, "です。", sep="")
# 上記とどちらが良いか検討要
# print("合計値は" + str(sum) + "です。")
