import sqlite3
import smtplib
from email.mime.text import MIMEText
con = sqlite3.connect('typing.db')


FROM = "testmailpython030@gmail.com"
TO = "ktq2590324@stu.o-hara.ac.jp"
PASSWORD = "urvd majr nwiu jriu"  # 16桁の英数字

# メール本文
msg = MIMEText("こんにちは！これはPythonから送ったテストメールです。")
msg["Subject"] = "テスト送信"
msg["From"] = FROM
msg["To"] = TO

# SMTP_SSLを使って送信
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(FROM, PASSWORD)
    smtp.send_message(msg)

print("送信完了！")