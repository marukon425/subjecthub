# 二つの数字を入力してください
while True:
    try:
        # １つ目の数字
        num1 = int(input('１つ目の数字を入力'))
        # ２つ目の数字
        num2 = int(input('２つ目の数字を入力'))
        # 〇+△=▢
        print(f'{num1} ÷ {num2} = {num1/num2}')
    except ValueError:
        print('数値以外を入力しないでください')
    # 0による除算の場合
    except ZeroDivisionError:
        print('0による除算はできません')
    
    # 例外処理が発生しなかった場合(正常に処理された場合)
    else:
        print('処理を終了します')
        break
    # 処理にかかわらず実行
    finally:
        print('またアプリを実行してね')