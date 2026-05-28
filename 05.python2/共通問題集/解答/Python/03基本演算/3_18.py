print("税込価格を求めます")

# 入力された定価を数値に変換して格納
price = int(input("定価："))
# 入力された消費税率を数値に変換して格納
tax = int(input("消費税率："))
# 税込価格を計算
result = int(price * (1 + tax / 100))

# 入力された定価の表示
print("定価 =", price)
# 入力された税率の表示
print("税率 =", tax)
# 税込価格の表示
print("税込価格 =", result)
