# モジュール(sqlite3)をインポート
import sqlite3

# 変数cinにshop.dbを繋ぐ
con = sqlite3.connect('shop.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()
# executeメソッドはSQQL実行 accountテーブルからすべて抽出
cur.execute('SELECT * FROM account')
# userとpasswordを一行ずつ表示
for user, password in cur:
    print(f'{user:10}{password}')
# 抽出だけしかしてないからcommitが不要
# コミットさせてDBを閉じる
con.commit()
con.close()
