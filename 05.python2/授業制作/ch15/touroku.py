# モジュール(sqlite3)をインポート
import sqlite3

# 変数cinにshop.dbを繋ぐ
con = sqlite3.connect('shop.db')

id = input('ログインIDを登録してください>>>')
pas = input('パスワードを登録してください>>>')

cur = con.cursor()
account = [(id, pas)]

cur.executemany('INSERT INTO account VALUES (?, ?)',
                account)

con.commit()
# コミットさせてDBを閉じる
con.close()
print('ログイン情報が保存されました')