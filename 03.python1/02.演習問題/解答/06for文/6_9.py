# 9×9の降順に奇数の段のみループして式と答えを表示
for i in reversed(range(1, 10, 2)):
    # 「〇の段」を表示
    print(i, "の段", sep="")
    for j in reversed(range(1, 10)):
        # 式と答えを表示
        print(i, "×", j, "=", i * j)
