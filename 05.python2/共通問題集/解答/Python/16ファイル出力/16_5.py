# endが入力されてるまで入力をくり返し、行番号を付加してファイルへデータを書き込む

file_name = input("ファイル名を入力：")
# ファイルを新規作成
write_file = open(file_name, "w")
write_file.close()

# データの入力
input_str_list = []

while True:
    input_str = input("入力：")

    # 入力値がendだったら入力を終了する
    if input_str == "end":
        print("書き込み終了")
        break

    # 入力値格納配列に追加
    input_str_list.append(input_str + "\n")

# ファイルを追記モードでオープン
add_file = open(file_name, "a")

# 行番号を付加してファイルにデータを書き込む
index = 1
for input_str in input_str_list:
    add_file.write(str(index) + "：" + input_str)
    index += 1

# ファイルをクローズする
add_file.close()
