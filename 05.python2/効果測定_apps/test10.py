# メール送信テスト
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

FROM = 'from.address@gmail.com' #送信元メールアドレス
PASSWORD = 'password' #送信元アカウントのパスワード
PORT = 587 #メールを送る際のポート番号(変更不要)

TO = 'to.address@gmail.com' #宛先
BCC = 'bcc.address@gmail.com' #s別宛先

SUBJECT = 'subject' #メールタイトル
BODY = 'message' #メール本文

def create_mail(from_addr, to_addr, bcc_addr, subject, body): #メール作成メソッド
    mail = MIMEText(body)
    # 以下で宛先等情報を入力
    mail["From"] = from_addr
    mail['To'] = to_addr
    mail['Bcc'] = bcc_addr
    mail['Subject'] = subject
    mail['Date'] = formatdate()
    return mail

def send_mail(to_addrs, mail): #メール送信メソッド
    smtpobj = smtplib.SMTP('smtp.gmail.com', PORT)
    smtpobj.ehlo()
    smtpobj.starttls() #暗号化
    smtpobj.ehlo()
    smtpobj.login(FROM, PASSWORD) #アカウントにログイン
    smtpobj.sendmail(FROM, to_addrs, mail.as_string()) #作成したメールを送信
    smtpobj.close()


if __name__ == '__main__': #メイン処理
    mail = create_mail(FROM, TO, BCC, SUBJECT, BODY)
    send_mail(TO, mail)