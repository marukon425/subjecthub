# 入力された月（数値）に該当する季節を表示する

# 月の連想配列を作成
season_dict = {1 : "冬",
               2 : "冬",
               3 : "春",
               4 : "春",
               5 : "春",
               6 : "夏",
               7 : "夏",
               8 : "夏",
               9 : "秋",
              10 : "秋",
              11 : "秋",
              12 : "冬"}

month = int(input("月を入力："))
if month < 1 or month > 12:
    print("対象の月はありません")
else:
    print(season_dict[month], "です", sep="")
