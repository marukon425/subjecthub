# 各商品に金額を設定
hamburger = 450
shake = 200
cola = 100

# 合計額（税抜）
sum = hamburger + shake + cola
# 消費税
tax = int(sum * 0.1)
# チップ
chip = int(sum * 0.16)
# 合計額（税込）
total = sum + tax + chip

# 計算結果の表示
print("ハンバーガー\t：", hamburger)
print("シェイク\t：", shake)
print("コーラ\t\t：", cola)
print("合計額（税抜）\t：", sum)
print("消費税\t\t：", tax)
print("チップ\t\t：", chip)
print("合計額（税込）\t：", sum + tax + chip)
