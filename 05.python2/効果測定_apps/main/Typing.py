import sqlite3
from CtrDB import CtrDB
class Typing:
    # 初期メソッド
    def __init__(self):
        self.con = sqlite3.connect('typing.db')
        self.cur = self.con.cursor()
        # データベース操作系のメソッド
        self.db = CtrDB()