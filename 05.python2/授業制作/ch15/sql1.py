# モジュール(sqlite3)をインポート
import sqlite3

# 変数cinにshop.dbを繋ぐ
con = sqlite3.connect('shop.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()
# executeメソッドはSQLの実行
# accountテーブルが残ってる場合は、削除(過去のデータを削除する場合)
cur.execute('DROP TABLE IF EXISTS account')
# accountテーブルを作成(user列, password列)
cur.execute('CREATE TABLE account \
            (user TEXT PRIMARY KEY, password TEXT)')
con.commit()
# コミットさせてDBを閉じる
con.close()