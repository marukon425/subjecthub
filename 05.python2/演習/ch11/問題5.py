'''
コンストラクタ：初期メソッド

Personクラス作る
個人情報（氏名、年齢、性別、身長(cm)、体重(kg)）を表示するメソッド
BMI値を求めるメソッド
肥満度を求めるメソッド
適正体重を求めるメソッド
'''

# クラス
class Person:
    def __init__(self, name, age, gender, height, weight):
        self.name = name
        self.age = int(age)
        self.gender = gender
        self.height = float(height)
        self.weight = float(weight)

    # 個人情報を表示するメソッド
    def person(self):
        print(f'名前：{self.name}  年齢：{self.age} 性別：{self.gender} 身長(cm)：{self.height} 体重(kg)：{self.weight}')

    # BMIを求めるメソッド
    def bmi(self):
        # BMI = 体重 (kg) ÷ 身長 (m)の2乗 
        print(f'BMI 値 = {float(self.weight/(self.height*self.height))}') 

    # 肥満度を求めるメソッド
    def overweight(self):
        bmi = float(self.weight/(self.height*self.height))
        if bmi < 16:
            print('やせすぎ')
        elif bmi < 17:
            print('痩せ')
        elif bmi < 18.5:
            print('痩せ気味')
        elif bmi < 25:
            print('普通')
        elif bmi < 35:
            print('肥満(1)')
        elif bmi < 40:
            print('肥満(2)')
        else:
            print('肥満(3)')
    
    # 適正体重を求めるメソッド
    def desirable_weight(self):
        print(f'適正体重 = {self.height * self.height * 22}')



# メイン
# クラスを使用して2名分のデータを作成
a = Person('丸山', 19, '男', 183, 75)
b = Person('尾田', 19, '男', 153, 75)
a.person()
a.bmi()
a.overweight()
a.desirable_weight()
