class DividedByZero(BaseException):
    """ ユーザ定義例外「０で割り算した場合」 """
    pass

def division(num1, num2):
    """ 割り算を行い結果を返却。ただしnum2が0の場合は DividedByZero を送出 """
    if num2 == 0:
        # 例外を送出
        raise DividedByZero
    else:
        return num1 / num2

# 数値を２つ入力
input_num1 = int(input('数値１ = '))
input_num2 = int(input('数値２ = '))

try:
    # 割り算を実行する関数の呼び出し
    answer = division(input_num1, input_num2)
except DividedByZero:
    print('０で割りました！！')
else:
    print('{} / {} = {}'.format(input_num1, input_num2, answer))
