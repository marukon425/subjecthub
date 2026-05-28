# モジュール(sqlite3)をインポート
import sqlite3

# 変数cinにshop.dbを繋ぐ
con = sqlite3.connect('shop.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()

user = 'suzuki'
password = 'cba321'
# ユーザー名が一致したとこにパスワードの変更をする
cur.execute('UPDATE account SET password=? WHERE user=?',
            (password, user))
con.commit()
con.close()