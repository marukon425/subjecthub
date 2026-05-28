# 入力されたファイル名に該当するファイルのデータを
# 指定されたファイル名でファイル作成し書き込む

# ファイルを読み込みモードで開く
read_file = open("16_9_read.txt", "r")
# ファイルを書き込みモードで開く
write_file = open("16_9_sum.txt", "w")

line_list = read_file.read().splitlines()

for line in line_list:
    # カンマで区切って配列に格納
    str_list = line.split(",")

    # 合計値を算出
    sum = 0
    for s in str_list:
        sum += int(s)

    # 合計値を末尾に追加
    str_list.append(str(sum) + "\n")
    # 1行分のデータをカンマ区切りで書き込み
    write_file.write(",".join(str_list))

# ファイルをクローズする
read_file.close()
write_file.close()
