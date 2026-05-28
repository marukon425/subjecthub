

import sqlite3
import time
from abc import *
import os
from email.mime.text import MIMEText
from email.utils import formatdate
from TypingMain import TypingMain
from PaintBackground import PaintBackground 
from PaintText import PaintText
from Mail import Mail

txt_paint = PaintText()
txt_back = PaintBackground()
con = sqlite3.connect('typing.db')
cur = con.cursor()

print('========タイピングゲーム========',end=time.sleep(2))
print('ユーザーネームを登録します',end=time.sleep(2))
print('前回のデータを引き継いで遊びたい場合は「ログイン」と入力して前回と同じユーザーネームを入力してください',end=time.sleep(2))
# 新規で登録したらユーザーネームのテーブルも新規で作る ※まだ未実装
name = input('>>>')
cm = TypingMain()
name = cm.user(name)
print(txt_back.red(f'{name}でログイン'),end=time.sleep(3))
time.sleep(3)
os.system('cls')
print('タイピングゲームを始めます',end=time.sleep(2))
print('☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ルール説明☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆ ☆',end=time.sleep(2))
print('制限時間内に多くの問題を解けば解くほど得点が多くなります',end=time.sleep(2))
print('制限時間は60秒です',end=time.sleep(2))
print(f'回答を入力するときは{txt_back.red("ひらがな")}で回答してください',end=time.sleep(2))
print('中断したい場合は「stop」を入力して中断してください',end=time.sleep(2))
# 中断した場合
while True:
    result = cm.main_game(name)
    if result == False:
        print('最初からやり直しますか？[ y / n ]')
        selection = input('>>>')
        if selection == 'y':
            continue
        elif selection == 'n':
            print('アプリを終了します')
            break
    elif result == True:
        print('もう一度遊びますか?[ y / n ]')
        selection = input('>>>')
        if selection == 'y':
            continue
        elif selection == 'n':
            con.close()
        
        try:
            while True:
                print('過去の成績を見ますか？[ y / n ]')
                select = input('>>>')
                if select == 'y':
                    os.system('cls')
                    cm.see_result(name)
                    time.sleep(3)
                    pass
                    break
                elif select == 'n':
                    pass
                    break
                else:
                    print('yかnで入力してください')
        except:
            print('予測できない入力がされたので強制終了します')
        else:
            # 参考 https://www.sejuku.net/blog/70497
            print('自分の成績をメールに送信しますか？[ y / n ]')
            select = input('>>>')
            if select == 'y':
                mail = Mail(input('宛先のメールアドレスを入力>>>'))
                body = mail.create_body(name)
                create = mail.create_mail(body)
                mail.send_mail(create)
                break
            elif select == 'n':
                break

print('アプリを終了します')
con.close()