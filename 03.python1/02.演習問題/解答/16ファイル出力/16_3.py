# ファイルへデータを書き込む

# ファイルを書き込みモードでオープン
write_file = open("16_3_write.txt", "w")
# ファイルにデータを書き込む
write_file.write("Hello\n")
# ファイルをクローズする
write_file.close()
