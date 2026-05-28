# endが入力されてるまで入力をくり返し入力されたデータをファイルへ書き込む

input_str_list = []

while True:
    input_str = input("入力：")

    # 入力値がendだったら入力を終了する
    if input_str == "end":
        print("書き込み終了")
        break

    # 入力値格納配列に追加
    input_str_list.append(input_str + "\n")

# ファイルを書き込みモードでオープン
write_file = open("16_4_write.txt", "w")
# ファイルにデータを書き込む
write_file.writelines(input_str_list)
# ファイルをクローズする
write_file.close()
