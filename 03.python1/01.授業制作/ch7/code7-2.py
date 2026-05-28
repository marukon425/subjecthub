### ファイル操作(開いたファイルを自動的に閉じる)

# ファイルに書き込みたいデータを入力
text = input('きょうは何をした？>>>')

# ファイルを開き、操作終了後に自動的に閉じる
# with open(ファイル名, モード) as オブジェクト名：
with open('diary.tet', 'a', encoding='utf-8') as file:
    # データを書き込み
    file.write(text + '\n')