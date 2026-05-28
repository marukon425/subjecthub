# 計算実行と結果の表示

class Calculator:
    """ 電卓クラス """

    def calc_sum(self, x: int, y: int) -> int:
        """ 合計値を取得 """        
        return x + y

    def calc_ave(self, x: int, y: int) -> int:
        """ 平均値を取得 """
        return (x + y) /2

class MoreCalc(Calculator):
    """ 電卓拡張クラス """

    """ 累乗を取得 """
    def calc_pow(self, x: int, y: int) -> int:
        return x ** y

# メインクラスの生成とメイン処理実行
num1 = int(input("整数を入力してください："))
num2 = int(input("整数を入力してください："))

more_calc = MoreCalc()
# 合計値
sum = more_calc.calc_sum(num1, num2)
print("Sum {} and {} = {}".format(num1, num2, sum))
# 平均値
ave = more_calc.calc_ave(num1, num2)
print("Average {} and {} = {}".format(num1, num2, ave))
# 累乗
pow = more_calc.calc_pow(num1, num2)
print("Power {} of {} = {}".format(num1, num2, pow))
