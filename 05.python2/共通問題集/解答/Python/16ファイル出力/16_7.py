# ファイルからデータを読み込む
# splitメソッドを使用して読み込んだデータを分割

# ファイルをリードモードでオープン
read_file = open("16_7_read.txt", "r")
# ファイルからデータを読み込む
raw_data = read_file.read()
# ファイルをクローズする
read_file.close()

# 読み込んだデータを改行で区切る
str_list = raw_data.split("\\n")

# 表示
for s in str_list:
    print(s)
