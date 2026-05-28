'''
今日は 〇月〇日です

ラッキーナンバーは〇〇です　※1～100

今日の運勢は「大吉？吉？小吉？など」です
'''
import datetime
import random

now = datetime.datetime.now()
print(f"今日は{now.month}月{now.day}日です")

n = random.randint(1, 100)
print(f"ラッキーナンバーは{n}です")

a = random.randint(1,5)
if a == 0:
    print("今日の運勢は大凶です")
elif a == 1:
    print("今日の運勢は凶です")
elif a == 2:
    print("今日の運勢は末吉です")
elif a == 3:
    print("今日の運勢は吉です")
elif a == 4:
    print("今日の運勢は小吉です")
else:
    print("今日の運勢は大吉です")