# "千代田"を"中央"に置換して表示

address_str = "東京都千代田区神田神保町千代田ビル１階"

# 出現する回数
count = address_str.count("千代田")

# 文字列の置換
result_str = address_str.replace("千代田", "中央")

# 文字列の表示
print(result_str)
print("置換した個数：", count)
