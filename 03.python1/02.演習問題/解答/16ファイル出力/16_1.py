# ファイルからデータを読み込みそのまま表示

# ファイルを開く(読込・テキストモード)
read_file = open("16_1_read.txt", "rt")

# ファイルからデータ読み込み
data = read_file.read()

# 読み込んだデータを表示
print(data)

# ファイルを閉じる
read_file.close()
