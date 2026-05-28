######################### ファイルの操作 #########################
# (ファイルを開く、データを書き込む)

# 書き込みたいデータを入力
text = input("何を入力しますか？")

# ファイルを開き、オブジェクト変数fileに代入
# 変数名　=　open(ファイル名, モード)
# モード：r 読み込み(read)  w 書き込み(write)　a 追記(追加:append)
file = open('diary.tet','a')
# diary.tetがない場合は、自動的に新規作成される

# diary.tet(fileオブジェクト) に入力したデータ(text)を書き込み
file.write(text +'\n') # \n:改行

# diary.tetを閉じる
file.close

