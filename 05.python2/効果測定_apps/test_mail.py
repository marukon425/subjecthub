import sqlite3
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
con = sqlite3.connect('typing.db')
cur = con.cursor()
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
        smtpobj = smtplib.SMTP('smtp.gmail.com', self.PORT)
        smtpobj.ehlo()
        smtpobj.starttls() #暗号化
        smtpobj.ehlo()
        smtpobj.login(self.FROM, self.PASSWORD) #アカウントにログイン
        smtpobj.sendmail(self.FROM, self.TO, mail.as_string()) #作成したメールを送信
        smtpobj.close()


mail = Mail(input('宛先のメールアドレスを入力>>>'))
body = mail.create_body('まる')
create = mail.create_mail(body)
mail.send_mail(create)
