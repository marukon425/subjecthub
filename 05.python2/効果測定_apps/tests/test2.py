import sqlite3
# typing.dbにアクセスする
con = sqlite3.connect('typing.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()

cur.execute('ALTER TABLE テーブル名 ADD COLUMN カラム名 データ型;')

con.commit()
con.close()