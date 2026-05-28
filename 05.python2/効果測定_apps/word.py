# タイピングの単語をDBに格納するためのプログラム

import sqlite3

# typing.dbにアクセスする
con = sqlite3.connect('typing.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()
# wordテーブルを作成(user列, password列)
cur.execute('CREATE TABLE userdata(user_name TEXT PRIMARY KEY , score TEXT,  play_itme TEXT )')  # tableを作成する指示

con.commit()
# 終了
con.close()

