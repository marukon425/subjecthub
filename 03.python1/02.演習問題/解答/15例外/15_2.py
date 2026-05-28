# 偶数か奇数か判定し結果を表示

try:
    num = int(input("整数を入力 = "))

    # 偶数奇数判定
    if num % 2 == 0:
        print("{}は偶数".format(num))
    else:
        print("{}は奇数".format(num))

except ValueError:
    print("整数と認識できません！！")
