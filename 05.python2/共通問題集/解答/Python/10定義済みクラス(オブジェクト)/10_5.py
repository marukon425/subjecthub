# 現在の日付と時刻を表示
import datetime

wd_list = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']

# 現在日時を取得
dt_now = datetime.datetime.now()

# 50日後を算出
after_fifty_days = dt_now + datetime.timedelta(days=50)

# 50日後の曜日を取得
wd = wd_list[after_fifty_days.weekday()]

# 日付と時刻を表示
print("今日は、", dt_now.year, "年", dt_now.month, "月", dt_now.day, "日です。", sep="")
print("今日の50日後は、", after_fifty_days.year, "年", after_fifty_days.month, "月", after_fifty_days.day, "日です。", sep="")
print("その日は、", wd, "です。", sep="")
