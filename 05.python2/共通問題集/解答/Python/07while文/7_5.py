# 1から100までの値で3の倍数以外を表示する
num = 1

while num <= 100:
    if num % 3 == 0:
        # 3の倍数は表示しない
        num += 1
        continue

    # 3の倍数ではないので表示する
    print(num)
    num += 1
