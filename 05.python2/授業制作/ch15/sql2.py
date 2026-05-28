# モジュール(sqlite3)をインポート
import sqlite3

# 変数cinにshop.dbを繋ぐ
con = sqlite3.connect('shop.db')
# DBを操作するカーソルオブジェクトをcur変数に代入

# [ , ]:リスト(変更可能)
# ( , ):タプル(変更不可)
# リストの中にタプルを格納する二次元配列を作成
cur = con.cursor()
account = [('suzuki', 'abc123'), 
            ('satou', 'def456'),
            ('tanaka', 'ghi789')]

# executemanyメソッドは、リストに対するSQL
# accountを挿入(データを追加)
cur.executemany('INSERT INTO account VALUES (?, ?)',
                account)
con.commit()
# コミットさせてDBを閉じる
con.close()
