# 二つの数字を入力してください
while True:
    try:
        # １つ目の数字
        num1 = int(input('１つ目の数字を入力'))
        # ２つ目の数字
        num2 = int(input('２つ目の数字を入力'))
        break
    # 数値以外の場合は例外処理「数値以外は入力しないでください」
    except:
        print('数値以外は入力しないでください')
# 〇+△=▢
print(f'{num1} + {num2} = {num1+num2}')
# 処理をしゅうりょうします
print('処理を終了します')