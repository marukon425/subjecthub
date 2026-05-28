# モジュール(sqlite3)をインポート
import sqlite3

# 変数cinにshop.dbを繋ぐ
con = sqlite3.connect('shop.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()
# executeメソッドはSQQL実行 accountテーブルからすべて抽出
cur.execute('SELECT * FROM account')

id = input('ユーザー名を入力してください>>>')
pas = input('パスワードを入力してください>>>')

F = False

# userとpasswordを一行ずつ表示
for user, password in cur:
    if user == id and password == pas:
        F = True
        print('成功')
if F == False:
    print('失敗')
# 抽出だけしかしてないからcommitが不要
con.commit()
# コミットさせてDBを閉じる
con.close()
