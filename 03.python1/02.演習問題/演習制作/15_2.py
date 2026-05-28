while True:
    try:
        num1 = int(input('整数を入力>>>'))
        if num1 % 2 == 0:
            print(f'{num1}は偶数')
        else:
            print(f'{num1}は奇数')
            break
    except ValueError:
        print('整数と認識できません！！')