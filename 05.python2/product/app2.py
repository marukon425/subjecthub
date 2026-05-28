import copy
class Money:
    def __init__(self, balance):
        self.balance = int(balance)
    
    histry = []

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
        self.balance += int(money)
        # 二次元配列で入出金を確認
        self.histry.append([f'入金',f'科目：{subject}', f'金額：{self.balance-money}'])

    # 履歴を返す
    def get_historys(self): 
        return copy.copy(self.histry)

    # 残高を返す
    def get_balance(self): 
        return self.balance


# スーパークラス
class File:
    def __init__(self, path):
        self.path = path

# テキストファイルを管理するクラス（fileクラスを継承）
class Filetxt(File):
    # __init__は変更がないため
    def set_txt(self,val):
    # ファイル書き込みモードで開く
        # valの引数の値でファイルに書き込み
        with open(self.path, 'w', encoding='utf-8')as file:
            file.write(str(val))

    def get_txt(self):
        # ファイルを読み込みモードで開く
        with open(self.path, encoding='utf-8')as file:
            # テキストファイルの中身を読みこんで、呼び出し元に戻す
            return file.read()




# Moneyのサブクラス
class MoneyTxt(Money):

    def balance_init(self, balance_path) :
        # テキストファイルからデータ取得時にファイルに何も書き込まれてないorデータが存在してなかったら
        # 残高の初期値の入力を求めて、その値を初期値として設定する
        
        try:
            # ☆ ファイルがあった場合
            # Filetxtをインスタンス化(ファイルを操作でいるようにファイル名を設定
            self.balance_txt = Filetxt(balance_path)
            # ファイルから残高を読み取り、残高を設定
            self.balance = self.balance_txt.get_txt()
            
        except:
            # 残高を入力
            self.balance = int(input('残高を入力'))
            

    # 残高の初期化
    def __init__(self, balance_path):
        # 残高の初期化
        self.balance_init(balance_path)
        # 履歴の初期化
        self.histry = []
        self.balance_path = balance_path

    # ファイルに書きもむメソッド
    def save(self):
        # 戻り値を持たない、データを保存するメソッド
        '''
        データ属性のFileTxt クラスの set_txt メソッドを使用し、データ属性の balance 変数の
        値をテキストファイルに書き込みます。
        '''
        # Filetxtクラス(balance_txtとしてインスタンス化)のset_txtメソッド
        self.balance_txt.set_txt(self.balance)
# =============================メイン===========================

'''
使用するクラスをMoneyクラスからMoneyTxtクラスに変更をします。 
修正箇所は以下の通りです。 
・import 文 
・Moneyクラスのインスタンス化処理、および引数の値をMoneyTxtクラスに変更 
・プログラムの終了時にMoneyTxtクラスのsaveメソッドを呼び出す
'''
print('--------家計簿アプリ--------')
# ファイル名を引数として
cm = MoneyTxt('balance.txt')
while True:
    print('残高と履歴の確認は［１］を入力')
    print('入金の登録は［２］を入力')
    print('出金の登録は［３］を入力してください')
    print('終了は［０］を入力してください')
    
    
    a = int(input())
    if a == 1:
        # 履歴の表示

        print('残高の確認をします')
        history = cm.get_historys()
        # ↓デバッグで二次元配列を表示
        print(f'残高：{cm.get_balance()}')
        for i in range(len(history)):
            print('-----------------------------------')
            print(history[i][0])
            print(history[i][1])
            print(history[i][2])

        
    # 入金
    elif a == 2:
        print('入金の登録をします')
        in_subjects = input('科目を入力して下さい。>>>')
        while True:
            try:
                in_pay = int(input('入金する額を入力してください。>>>'))
                break
            except:
                print('正しい金額を入力してください')
        cm.set_payment(in_subjects, in_pay)
    # 出金
    elif a == 3:
        print('出金をします')
        in_subjects = input('科目を入力してください>>>')
        while True:
            try:
                in_pay = int(input('入金する額を入力してください。>>>'))
                break
            except:
                print('正しい金額を入力してください')
        if cm.set_withdrawal(in_subjects, in_pay) == False:
            print('残高が足りないので出金できませんでした')
    elif a == 0:
        # 残高をファイルに保存
        cm.save()
        print('家計簿アプリを終了します')
        break
    else:
        print('正しい数値を入力してください')
