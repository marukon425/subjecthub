# 「0除算」例外を補足

try:
    num1 = int(input("整数１ = "))
    num2 = int(input("整数２ = "))

    # 除算結果の表示
    print("{} / {} = {}".format(num1, num2, num1 / num2))

except ZeroDivisionError:
    print("０によるわり算です！！")

finally:
    print("処理終了")
