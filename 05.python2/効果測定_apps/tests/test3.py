import sqlite3
# typing.dbにアクセスする
con = sqlite3.connect('typing.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()


cur.execute("SELECT word_level, japanese FROM word WHERE word = ?", ('ゆき',))
rows = cur.fetchall()


# データを出力（[]と()を外して変数に代入）
for row in rows:
    word_level, japanese = row
    print(word_level, japanese)


con.commit()
con.close()