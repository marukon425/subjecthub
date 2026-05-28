# 二つの数字を入力してください
while True:
    try:
        # １つ目の数字
        num1 = int(input('１つ目の数字を入力'))
        # ２つ目の数字
        num2 = int(input('２つ目の数字を入力'))
        # 〇+△=▢
        print(f'{num1} ÷ {num2} = {num1/num2}')
        break
    # 0による除算の場合
    except ZeroDivisionError:
        print('0による除算はできません')

# 〇+△=▢
print(f'{num1} ÷ {num2} = {num1/num2}')
# 処理を終了します
print('処理を終了します')