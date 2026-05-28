# ファイルからデータを読み込む
# splitメソッドを使用して読み込んだデータを分割

# ファイルをリードモードでオープン
read_file = open("16_6_read.txt", "r")
# ファイルからデータを読み込む
raw_data = read_file.read()
# ファイルをクローズする
read_file.close()

# 読み込んだデータを「、」で区切る
sp_list = raw_data.split('、')

# 1要素ずつ表示
for sp in sp_list:
    print(sp)
