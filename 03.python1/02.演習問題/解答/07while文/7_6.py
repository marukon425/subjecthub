# 0が入力されるまで数値を合算し合計値と平均値を表示する
cnt = 0
sum = 0

while True:
    num = int(input("整数を入力："))
    if num == 0:
        # 0が入力されたら入力を終了
        break

    # 入力値を加算する
    cnt += 1
    sum += num

print("合計値：", sum)
print("平均値：", sum/cnt)
