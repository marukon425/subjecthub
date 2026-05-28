# 設定された10人分の点数を元に偏差値を求めて表示
import statistics

# 点数リスト
score_list = [50, 68, 48, 92, 58, 79, 89, 60, 74, 69]

# 平均点
ave = statistics.mean(score_list)
# 標準偏差
std = statistics.pstdev(score_list)

# 偏差値を表示
index = 1
for score in score_list:
    pt = (score - ave) / std * 10 + 50
    print(index, "人目の偏差値は", round(pt, 1), sep="")
    index += 1
