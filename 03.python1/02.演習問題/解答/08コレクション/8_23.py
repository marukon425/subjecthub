# 入力された月（数値）に該当する英語表記を表示する

# 月の連想配列を作成
month_dict = {1 : "January",
              2 : "February",
              3 : "March",
              4 : "April",
              5 : "May",
              6 : "June",
              7 : "July",
              8 : "August",
              9 : "September",
             10 : "October",
             11 : "November",
             12 : "December"}

month = int(input("月を入力："))
if month < 1 or month > 12:
    print("対象の月はありません")
else:
    print(month_dict[month])
