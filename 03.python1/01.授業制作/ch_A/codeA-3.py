# 例外処理(try except)の学習


'''
料金と人数を入力し、
一人当たりの割り勘金額の表示
'''
## 料金と人数を入力時に 文字などを入力されるかも ##
'''
例外処理の書き方
try:
    エラーになるかも知れない
except エラー名：

'''

try: #エラーになるかも知れない処理
    # 料金を入力
    mony = int(input('料金を入力>>>'))
    # 人数を入力
    people = int(input('人数を入力>>>'))
    # 割り勘料金を出力
    print(f'一人当たりの金額は{mony/people}円です。')
except ValueError: # エラー時の処理
    print('料金と人数は整数を入力してください')
except ZeroDivisionError: # ZeroDivisionError : 0で割り算できない時に出てくるエラー
    print('人数には０を入力できません')
# try-except終了後に表示
print('プログラム終了')

