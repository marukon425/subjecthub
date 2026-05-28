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
        self.balance += money
        # 二次元配列で入出金を確認
        self.histry.append([f'入金',f'科目：{subject}', f'金額：{self.balance-money}'])

    # 履歴を返す
    def get_historys(self): 
        return copy.copy(self.histry)

    # 残高を返す
    def get_balance(self): 
        return self.balance


# =============================メイン===========================
cm = Money(400)
print(f'現在の残高：{cm.get_balance()}')

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
        print(history)
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
        print('家計簿アプリを終了します')
        break
    else:
        print('正しい数値を入力してください')
