import sqlite3
class CtrDB:
    def __init__(self):
        self.con = sqlite3.connect('typing.db')
        self.cur = self.con.cursor()

    # ユーザーネーム検索
    def serch_name(self, name):
        self.cur.execute('SELECT ユーザーネーム FROM ユーザー WHERE ユーザーネーム = ?', (name,))
        serch = self.cur.fetchone()
        return serch
    # ユーザー登録
    def reg_name(self, name):
        self.cur.execute('INSERT INTO ユーザー VALUES (?)', (name,))
        self.cur.execute(f'CREATE TABLE IF NOT EXISTS "{name}" (遊んだ日 TEXT PRIMARY KEY, 答えた数 TEXT, 間違えた回数 TEXT)')
        self.con.commit()