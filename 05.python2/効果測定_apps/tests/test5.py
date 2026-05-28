import sqlite3

# データベースに接続（存在しない場合は作成される）
conn = sqlite3.connect('sample.db')
cursor = conn.cursor()

# サンプルテーブルの作成（必要に応じて）
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
''')

# サンプルデータの挿入（初回のみ）
sample_names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
cursor.executemany('INSERT INTO users (name) VALUES (?)', [(name,) for name in sample_names])
conn.commit()

# ランダムに1件抽出
cursor.execute('SELECT * FROM users ORDER BY RANDOM() LIMIT 1')
random_record = cursor.fetchone()

print("ランダムに抽出されたレコード:", random_record)

# 接続を閉じる
conn.close()

# SELECT * FROM users WHERE id < 5 ORDER BY RANDOM() LIMIT 1 