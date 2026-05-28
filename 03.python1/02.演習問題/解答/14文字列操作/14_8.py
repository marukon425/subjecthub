# 区の名前だけを抜き出して表示

address_str = "東京都千代田区神田神保町"
target_str = "東京都"

# 東京都の出現要素番号を取得
index1 = address_str.index(target_str)

# 区名の開始位置と終了位置を特定
start = index1 + len(target_str)
end = address_str.index("区") + 1

# 文字列を抜き出して表示
print(address_str[start:end])
