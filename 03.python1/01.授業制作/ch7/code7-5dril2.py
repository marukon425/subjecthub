# 標準ライブラリの復習
# 標準ライブラリ：pythonをインストールした時点で入っているモジュール
'''
乱数を発生：●
きょうは●月●日
'''

import random
from datetime import datetime
# 関数aに乱数（１－１００）を発生
a = random.randint(1,100)
print(f"乱数を発生：{a}")

# 関数bに日付を入れる
# b = datetime.datetime.now()
# print(f"今日は{b.month}月{b.day}日")
# 別解
# 今日の日付を所得
today = datetime.now()
# 今日の日付を表示
print(f"今日のは{today.month}月{today.day}日")