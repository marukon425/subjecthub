# 現在の日付と時刻を表示
import datetime

# 現在日時を取得
dt_now = datetime.datetime.now()

# 日付と時刻を表示
print("今日の日付は", dt_now.year, "年", dt_now.month, "月", dt_now.day, "日です。", sep="")
print("現在の時刻は", dt_now.hour, "時", dt_now.minute, "分", dt_now.second, "秒です。", sep="")
