# クラスを作成
import sqlite3
import copy
import csv

class Money:
    def __init__(self, balance):
        self.balance = int(balance)
        self.histry = []

    # 出金メソッド(subjectは科目)
    def set_withdrawal(self, subject, money):
        if self.balance - money < 0:
            return False
        else:
            self.balance = self.balance - money
            # 二次元配列で入出金を確認
            self.histry.append(['出金', f'科目：{subject}', f'金額：{self.balance-money}'])

    # 入金メソッド
    def set_payment(self, subject, money):
        self.balance += money
        # 二次元配列で入出金を確認
        self.histry.append([f'入金',f'科目：{subject}', f'金額：{self.balance-money}'])

    # 履歴を返す
    def get_historys(self): 
        return copy.copy(self.histry)

    # 残高を返す
    def get_balance(self): 
        return self.balance


    # 関数名　set_paymebt
    # 引数　　subuject,money
    # 戻り値　なし
    # 入金メソッド
    def set_paymebt(self,subuject,money):
        # 金額に足す
        self.balance += money
        # リストに追加
        self.history.append(["入金",subuject,str(money)])

    # 関数名　get_payment
    # 引数  
    # 戻り値  あり
    # 履歴
    def get_historys(self):
        self.deep_history = copy.deepcopy(self.history)
        return self.history
    # 関数名　get_balance
    # 引数    なし
    # 戻り値　なし
    # 残高確認
    def get_balance(self):
        return self.balance

# MoneyTxtクラスを作成（Moneyを継承）
class MoneyTxt(Money):
    def __init__(self, balance_path):
        # 残高の初期化
        self.balance_init(balance_path)
        # 履歴の初期化
        self.history = []
    def balance_init(self, balance_path):
        try:
            # インスタンス化
            self.Fi_ob = FileTxt(balance_path)
            # 書き込みメソッド呼び出し
            self.balance = int(self.Fi_ob.get_txt())
        except:
            # 例外処理
            self.balance = int(input("残高を入力>>>"))
    def save(self):
        # 保存
        self.Fi_ob.set_txt(self.balance)
# Fileクラスを作成
class File:
    # 初期化メソッド
    def __init__(self,path):
        self.path = path
# FileTxtクラスを作成（Fileクラス継承）
class FileTxt(File):
    def set_txt(self,val):
        # 書き込みメソッド
        with open(self.path, "w", encoding="utf-8") as fi:
            fi.write(str(val))
    def get_txt(self):
        # 読み込みメソッド
        with open(self.path, encoding="utf-8") as fi:
            val = fi.read()
        return val

class SqlManager:
    # 初期メソッド
    def __init__(self):
        # ショップDBに接続しcon変数に代入
        self.con = sqlite3.connect("shop.db")
        # データベースを操作するカーソルオブジェクトを　cur変数に代入
        self.cur = self.con.cursor()
        # executeメソッドは、SQLの実行
        # accountデーブルが存在する場合は、削除（過去のデータを削除したい場合）
        self.cur.execute("CREATE TABLE IF NOT EXISTS kakeibo (journal TEXT, subject TEXT, money INTEGER)")
        # データベースの処理を確定
        self.con.commit()
        # データベースを閉じる
        self.con.close()

    # データを取得して管理するメソッド
    def select_all(self):
        self.a = []
        # ショップDBに接続しcon変数に代入
        self.con = sqlite3.connect("shop.db")
        # データベースを操作するカーソルオブジェクトを　cur変数に代入
        self.cur = self.con.cursor()
        self.cur.execute("SELECT * FROM kakeibo")
        for x in self.cur:
            self.a.append(list(x))
        return copy.deepcopy(self.a)
    
    # データベースに書き込むメソッド
    def insert_all(self,lst):
        # ショップDBに接続しcon変数に代入
        self.con = sqlite3.connect("shop.db")
        # データベースを操作するカーソルオブジェクトを　cur変数に代入
        self.cur = self.con.cursor()
        # テーブルの中身をすべて削除
        self.cur.execute("DELETE FROM kakeibo")
        # データベースの処理を確定
        self.con.commit()
        # データベースを閉じる
        self.con.close()

        # ショップDBに接続しcon変数に代入
        self.con = sqlite3.connect("shop.db")
        # データベースを操作するカーソルオブジェクトを　cur変数に代入
        self.cur = self.con.cursor()
        # テーブルにレコードを追加する
        self.cur.executemany("INSERT INTO kakeibo VALUES(?,?,?)",lst)
        # データベースの処理を確定
        self.con.commit()
        # データベースを閉じる
        self.con.close()

class MoneyDB(MoneyTxt):
    # 初期設定
    def __init__(self, balance_path):
        self.sql_mo = SqlManager()
        self.balance_init(balance_path)
        self.history_init()

    def history_init(self):
        self.sql_mo = SqlManager()
        self.history = self.sql_mo.select_all()

    def save(self):
        super().save()
        self.sql_mo.insert_all(self.history)

# ==================================メイン==================================
print('--------家計簿アプリ--------')
balance_path = "histyo_db"
obj_me = MoneyDB(balance_path)
while True:
    print('残高と履歴の確認は［１］を入力')
    print('入出金処理は［２］を入力')
    print('終了は［０］を入力してください')
    try:
        selection = int(input(">>>>"))
    except:
        print("整数で入力")
    # 終了処理
    if selection == 0:
        obj_me.save()
        break
    #　入出金処理
    if selection == 2:
        print("戻るは１")
        print("入金は２")
        print("出金は３")
        try:
            selection1 = int(input("選択してください>>>>"))
        except:
            print("整数で入力")
        if selection1 == 1:
            continue
        # 入金処理
        if selection1 == 2:
            sub = input("科目を入力>>>")
            mon = int(input("金額を入金>>>"))
            obj_me.set_paymebt(sub,mon)
            print("入金されました")
            print(obj_me.get_balance())
            obj_me.save()
        # 出金処理
        if selection1 == 3:
            sub = input("科目を入力>>>")
            mon = int(input("金額を出金>>>"))
            obj_me.set_withdrawal(sub,mon)
            print("出金しました")
            print(obj_me.get_balance())
            obj_me.save()
    # 履歴確認処理
    if selection == 1:
        print(obj_me.get_historys())
print('家計簿アプリを終了します')