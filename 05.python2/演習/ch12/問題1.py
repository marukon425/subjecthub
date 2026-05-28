'''
継承
'''

# Calculatorを作る
class Calculatot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    # CalcSumを作る
    def CalcSum(self):
        return self.x + self.y
    
    # CalcAveを作る
    def CalcAve(self):
        return (self.x + self.y) / 2

# Calculatorから継承してMoreCalcを作る
class Calculator(Calculatot):
    
    def __init__(self, x, y):
        super().__init__(x, y)

    # CalcPowを作る
    def CalcPow(self):
        return self.x ** self.y
    


# メイン
x = int(input('整数を入力：'))
y = int(input('整数を入力：'))

a = Calculator(x, y)
print(f'Sum{x} and sum{y} = {a.CalcSum()}')
print(f'Average{x} and{y} = {int(a.CalcAve())}')
print(f'Power{x} of{y} = {a.CalcPow()} ')
