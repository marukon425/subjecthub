# ファイルからデータを読み込み、改行で分割して表示

# ファイルを読み込みモードでオープン
read_file = open("16_2_read.txt", "r")
# ファイルからデータを読み込む
raw_data = read_file.read()
# ファイルをクローズする
read_file.close()

# 読み込んだデータを改行で区切る
person_list = raw_data.splitlines()

# 表示
for person in person_list:
    print(person)
