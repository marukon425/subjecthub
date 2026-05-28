import sqlite3

# typing.dbにアクセスする
con = sqlite3.connect('typing.db')
# DBを操作するカーソルオブジェクトをcur変数に代入
cur = con.cursor()

cur.execute("ALTER TABLE ユーザー RENAME COLUMN user_name TO ユーザーネーム")
# ALTER TABLE テーブル名 RENAME TO 新しいテーブル名;
# 現在のテーブル一覧を確認
# alter table  rename old_name to new_name;
# ALTER TABLE users DROP COLUMN email;

'''
テーブルの存在を確認するプログラム
↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cur.fetchall())
'''
con.commit()
con.close()