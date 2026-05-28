# 「東京都」以外の部分を抜き出して表示

address_str = "東京都千代田区神田神保町"
target_str = "東京都"

# 東京都の出現要素番号を取得
index = address_str.index(target_str)

# 文字列を抜き出して表示
print(address_str[index + len(target_str):])
