# 9×9の昇順に2重ループして式と答えを表示
for i in range(1, 10):
    # 「〇の段」を表示
    print(i, "の段", sep="")
    for j in range(1, 10):
        # 式と答えを表示
        print(i, "×", j, "=", i * j)
