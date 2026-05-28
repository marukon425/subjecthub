# 1年間の勉強時間算出
sum = 0

# 1年=52週間分くり返し処理
for i in range(1, 53):
    # 表示用の「○週目」文字列を作成
    week_str = str(i) + "週目"
    print(week_str)

    # 1週間を表す繰り返し処理
    for j in range(1, 8):
        # 表示用の「…○時間」文字列を作成
        hour_str = "曜日…" + str(j) + "時間"
        holiday_str = "曜日…お休み"

        if j == 1:
            print(week_str, "月" + hour_str)
        elif j == 2:
            print(week_str, "火" + hour_str)
        elif j == 3:
            print(week_str, "水" + hour_str)
        elif j == 4:
            print(week_str, "木" + hour_str)
        elif j == 5:
            print(week_str, "金" + hour_str)
        elif j == 6:
            if i % 2 == 1:
                # 奇数週の土曜日はお休み
                print(week_str, "土" + holiday_str)
                continue
            else:
                # 土曜日がお休みではない場合
                print(week_str, "土" + hour_str)
        elif j == 7:
            if i % 2 == 0:
                # 偶数の週の日曜日はお休み
                print(week_str, "日" + holiday_str)
                continue
            else:
                # 日曜日がお休みではない場合
                print(week_str, "日" + hour_str)

        # 勉強時間を合算
        sum += j
        
    print()

# 勉強時間の合計値を表示
print("合計：", sum, "時間", sep="")
