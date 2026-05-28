import sqlite3
import datetime

# データベースに接続（存在しない場合は作成される）
con = sqlite3.connect('typing.db')
cur = con.cursor()

# 各ユーザーのテーブルを削除
# executeメソッドはSQQL実行 accountテーブルからすべて抽出
cur.execute('SELECT ユーザーネーム FROM ユーザー')
# リストにユーザーネームを追加
l =[]
for i in cur:
    l.append(i)
s = []
for i in l:
    for j in i:
        s.append(j)

# ユーザーの全テーブルを削除
for i in s:
    cur.execute(f'DROP TABLE IF EXISTS "{i}"',)



# ユーザーテーブルの内のレコードを全削除
for i in s:
    cur.execute(f"DELETE FROM ユーザー WHERE ユーザーネーム = '{i}'")



# 接続を閉じる
con.commit()
con.close()

