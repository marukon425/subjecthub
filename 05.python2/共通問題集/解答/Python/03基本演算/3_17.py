print("台形の面積を求めます")

# 上底の長さを入力
upper = float(input("上底の長さ："))
# 下底の長さを入力
bottom = float(input("下底の長さ："))
# 高さを入力
height = float(input("高さ："))

# 面積計算
area = (upper + bottom) * height / 2

# 結果表示
print("台形の面積 = ", area)
