
import sqlite3
import datetime
import time
from abc import *
import os
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

con = sqlite3.connect('typing.db')
cur = con.cursor()
# DBを操作するカーソルオブジェクトをcur変数に代入
# クラス部分
# ==========================================================================
# ターミナルに色を付けて出力するクラス(抽象クラス)
class Paint:
    @abstractmethod
    def black(self,text):
        pass
    @abstractmethod
    def red(self,text):
        pass
    @abstractmethod
    def green(self,text):
        pass
    @abstractmethod
    def yellow(self,text):
        pass
    @abstractmethod
    def blue(self,text):
        pass
    @abstractmethod
    def magenda(self,text):
        pass
    @abstractmethod
    def cyan(self,text):
        pass
    @abstractmethod
    def white(self,text):
        pass


# ターミナルに色を付けて出力する派生クラス(テキストに文字をつける)
class PaintText(Paint):
    def black(self,text):
        return '\033[30m'+text+'\033[0m'
    def red(self,text):
        return '\033[31m'+text+'\033[0m'
    def green(self,text):
        return '\033[32m'+text+'\033[0m'
    def yellow(self,text):
        return '\033[33m'+text+'\033[0m'
    def blue(self,text):
        return '\033[34m'+text+'\033[0m'
    def magenda(self,text):
        return '\033[35m'+text+'\033[0m'
    def cyan(self,text):
        return '\033[36m'+text+'\033[0m'
    def white(self,text):
        return '\033[37m'+text+'\033[0m'
# ターミナルに色を付けて出力する派生クラス(背景に色を付ける)
class PaintBackground(Paint):
    def black(self,text):
        return '\033[40m'+text+'\033[0m'
    def red(self,text):
        return '\033[41m'+text+'\033[0m'
    def green(self,text):
        return '\033[42m'+text+'\033[0m'
    def yellow(self,text):
        return '\033[43m'+text+'\033[0m'
    def blue(self,text):
        return '\033[44m'+text+'\033[0m'
    def magenda(self,text):
        return '\033[45m'+text+'\033[0m'
    def cyan(self,text):
        return '\033[46m'+text+'\033[0m'
    def white(self,text):
        return '\033[47m'+text+'\033[0m'

txt_paint = PaintText()
txt_back = PaintBackground()

# データベース操作系クラス
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

'''============基底クラス=========='''

class Typing:
    # 初期メソッド
    def __init__(self):
        self.con = sqlite3.connect('typing.db')
        self.cur = self.con.cursor()
        # データベース操作系のメソッド
        self.db = CtrDB()

'''===================================================='''

class TypingRog(Typing):
    
    # 初期メソッドは基底クラスで定義しているため必要なし
    # ユーザー登録(ログイン)するメソッド
    def user(self, username):
        # ログイン処理
        print('ユーザーネームを入力してください')
        while True:
            if username == 'ログイン':
                n = input('>>>')
                if self.db.serch_name(n):
                    print('ログインできました')
                    return n
                else:
                    print('ログインできません\n再度入力してログインしてください')
                    continue
                # 名前だけをuserdataテーブルに保存
                # 名前が存在してるか検索する
            else:
                if self.db.serch_name(username):
                    print('その名前は使われてます。再度入力してください')
                    continue
                else:
                    # 存在してない場合
                    # 新規登録
                    # ほかのデータはNULLで保存
                    self.db.reg_name(username)
                    print(txt_back.blue('登録できました'))
                    return username


class TypingNow(TypingRog):
    # 出題する問題を出すメソッド
    def question(self, level):
        # ランダムに単語を抽出
        question = self.cur.execute('SELECT word, japanese FROM 単語 WHERE word_level = ? ORDER BY RANDOM() LIMIT 1 ',(level,)).fetchone()
        # タプルになってる問題を返す
        return question
        
    # 出された問題に対して答えが合ってるか管理するメソッド
    def check_answers(self, answer, example_answer):
        if answer == example_answer:
            return True
        else:
            return False

class TypingMain(TypingNow):
    def __init__(self):
        super().__init__()
        self.cm = TypingNow()

    def main_game(self, name):
        ans_count = 0
        bat_count = 0
        print('準備ができたら適当なキーを入力して開始します',end=time.sleep(3))
        input('>>>')
        for i in range(6):
            if i == 5:
                print('スタート!')
            else:
                print(5-i)
                time.sleep(1)
        # タイピングゲーム中
        # レベルのカウンタの初期化
        level_count = 0
        # 始めた時間を記録
        start_time = time.time()
        # 60秒に設定
        while True:
            # 解くごとにレベルが１上がる
            level_count += 1
            # レベルが14以上になったら14に固定する
            if level_count >= 13:
                level_count = 13
            read, japan = self.cm.question(level_count)
            # ↑ ひらがな表記
            # 正解するまで繰り返す　正常↓
            while True:
                flg = True
                if flg == False:
                    print(txt_back.red('違います'))
                print(japan)
                ans = input('>>>')
                if ans == 'stop':
                    return False
                elif ans == 'teat':
                    ans = read
                    continue
                if self.cm.check_answers(ans, read) == True:
                    ans_count += 1
                    print('正解')
                    flg = True
                    os.system('cls')
                    break
                else:
                    bat_count += 1
                    print('違います')
                    flg = False
                    os.system('cls')
            # タイマー
            if time.time() >= start_time + 60:
                print('終了!!')
                # 成績を表示
                time.sleep(2)
                print('正解した数：',end='')
                time.sleep(1)
                print(f'{ans_count}問')
                time.sleep(1)
                print('間違えた数:',end='')
                time.sleep(1)
                print(f'{bat_count}回')
                time.sleep(1)
                # 成績をデータベースに保存
                t = datetime.datetime.now().strftime('%Y年%m月%d日%H時%M分%S秒')
                self.cur.execute(f'INSERT INTO "{name}" VALUES (?, ?, ?)',(t, ans_count, bat_count))
                self.con.commit()
                return True
    # 成績を見るメソッド
    def see_result(self, user_name):
        self.cur.execute(f'SELECT * FROM "{user_name}"')
        rows = self.cur.fetchall()
        # データを出力（[]と()を外して変数に代入）
        print(f'{user_name}の記録')
        for row in rows:
            play_day, ans, bat_ans = row
            print(f'{play_day}  |  答えた数：{ans}  |  間違えた数：{bat_ans}')

# メール送信をするクラス
# 参考 https://www.sejuku.net/blog/70497
class Mail:
    def __init__(self, to_mail):
        self.FROM = 'testmailpython030@gmail.com' #送信元メールアドレス
        self.PASSWORD = 'urvd majr nwiu jriu' #送信元アカウントのパスワード
        self.PORT = 587 #メールを送る際のポート番号(変更不要)

        self.TO = to_mail #宛先
        self.BCC = 'ktq2590324@stu.o-hara.ac.jp' #s別宛先

        self.SUBJECT = 'テスト' #メールタイトル
    # メールの本文を作成するメソッド(ユーザーネームをを引数として受け取る)
    # 本文を戻り値にする
    def create_body(self, user_name):

        # ↓ メール本文を格納する変数(すべて１行で格納する予定)
        body = f'{user_name}の記録\n'
        cur.execute(f'SELECT * FROM "{user_name}"')
        rows = cur.fetchall()
        for row in rows:
            play_day, ans, bat_ans = row
            body += f'遊んだ日：{play_day}  |  答えた数：{ans}  |  間違えた数：{bat_ans}\n'
        body += '\n'
        body += 'また遊んでね!!'
        return body


    def create_mail(self, body): #メール作成メソッド
        mail = MIMEText(body)
        # 以下で宛先等情報を入力
        mail["From"] = self.FROM
        mail['To'] = self.TO
        mail['Bcc'] = self.BCC
        mail['Subject'] = self.SUBJECT
        mail['Date'] = formatdate()
        return mail

    def send_mail(self,mail): #メール送信メソッド
        try:
            smtpobj = smtplib.SMTP('smtp.gmail.com', self.PORT)
            smtpobj.ehlo()
            smtpobj.starttls() #暗号化
            smtpobj.ehlo()
            smtpobj.login(self.FROM, self.PASSWORD) #アカウントにログイン
            smtpobj.sendmail(self.FROM, self.TO, mail.as_string()) #作成したメールを送信
            smtpobj.close()
        except:
            print(txt_back.red('何らかのエラーが発生したのでメールを送信できませんでした'))
        else:
            print(txt_back.blue('送信ができました!'))
# ===================================================メイン===================================================


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
            break
        break


else:
    try:
        print('過去の成績を見ますか？[ y / n ]')
        select = input('>>>')
        if select == 'y':
            os.system('cls')
            cm.see_result(name)
            time.sleep(3)
            pass
        elif select == 'n':
            pass
    except:
        print('何らかのエラーが起きたので見れませんでした')
    else:
        # 参考 https://www.sejuku.net/blog/70497
        print('自分の成績をメールに送信しますか？[ y / n ]')
        select = input('>>>')
        if select == 'y':
            mail = Mail(input('宛先のメールアドレスを入力>>>'))
            body = mail.create_body(name)
            create = mail.create_mail(body)
            mail.send_mail(create)
        elif select == 'n':
            pass

print('アプリを終了します')
con.close()