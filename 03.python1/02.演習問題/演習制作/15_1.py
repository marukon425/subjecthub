while True:
    try:
        num1 = int(input('整数１を入力>>>'))
        num2 = int(input('整数２を入力>>>'))
        print(f"{num1} / {num2} = {num1/num2}")
        break
    except ZeroDivisionError:
        print('0による割り算です！！')
