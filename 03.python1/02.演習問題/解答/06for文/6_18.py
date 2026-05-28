import math
# カレンダーを表示する
current_day = 1

print("カレンダーを表示させます。")
print("0:日　1:月　2:火　3:水　4:木　5:金　6:土")
start_day = int(input("表示させたい月は何曜日から始まりますか："))
day_cnt = int(input("表示させたい月は何日ありますか："))

# 週の数を求める
week_num = math.ceil((day_cnt + start_day) / 7)

# 曜日を表示
print()
print("日 月 火 水 木 金 土")

# 週の数でループ
for i in range(1, week_num+1):
    # 1行分の文字列を初期化
    row_str = ""

    # 曜日の数分ループ
    for j in range(0, 7):
        # 日にちが1桁の場合は半角SPで調整
        if len(str(current_day))== 1:
            row_str += " "

        # 1週目のみ開始曜日の判定を行う
        if i == 1 and start_day > j:
            # 開始の曜日ではないのでSPで埋める
            row_str += "　"
            continue

        # 現在の日にちを1行分の文字列に追加
        row_str += str(current_day) + " "

        # 末日チェック
        if current_day == day_cnt:
            # 指定された日に達しているので処理を終了
            break

        # 現在の日にちを更新
        current_day += 1

    # 1行分表示
    print(row_str)

print()



