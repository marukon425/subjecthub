import sqlite3
import datetime
con = sqlite3.connect('typing.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()
name = 'まる'
ans_count = 0
bat_count = 0
t = datetime.datetime.now().strftime('%Y年%m月%d日%H時%M分%S秒')
cur.execute(f'INSERT INTO "{name}" VALUES (?, ?, ?)',(t, ans_count, bat_count))
con.commit()