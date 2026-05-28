import math

class Person:
    """ 人間クラス """ 

    # 名前
    __name = ""
    # 年齢
    __age = 0
    # 性別
    __gender = "" 
    # 身長(cm)
    __height = 0.0 
    # 体重(Kg)
    __weight = 0.0 
 
    # コンストラクタ
    def __init__(self, name: str, age: int, gender: str, height: float, weight: float) -> None:
        self.set_name(name)
        self.set_age(age)
        self.set_gender(gender)
        self.set_height(height)
        self.set_weight(weight)

    # 名前を取得
    def get_name(self) -> str:
        return Person.__name
    
    # 年齢を取得 
    def get_age(self) -> int:
        return Person.__age

    # 性別を取得
    def get_gender(self) -> str:
        return Person.__gender     

    # 身長(cm)を取得 
    def get_height(self) -> float:
        return Person.__height

    # 体重(Kg)を取得
    def get_weight(self) -> float:
        return Person.__weight 

    # 名前を設定
    def set_name(self, name: str) -> None:
        Person.__name = name

    # 年齢を設定
    def set_age(self, age: int) -> None:
        if age < 0:
            Person.__age = 0
        else:
            Person.__age = age

    # 性別を設定
    def set_gender(self, gender) -> None:
        Person.__gender = gender

    # 身長(cm)を設定 
    def set_height(self, height: float) -> None:
        if height < 0.0:
            Person.__height = 0.0
        else:
            Person.__height = height

    # 体重(Kg)を設定
    def set_weight(self, weight: float) -> None:
        if weight < 0.0:
            Person.__weight = 0.0
        else:
            Person.__weight = weight

    # 個人情報を表示
    def disp_info(self):
        print("名前：{} 年齢：{} 性別：{} 身長(cm)：{} 体重(Kg)：{}".format(Person.__name, Person.__age, Person.__gender, Person.__height, Person.__weight))

    # BMI値を計算して返却
    def get_bmi(self) -> float:
        bmi = Person.__weight / ((Person.__height/100) ** 2)
        return math.floor(bmi * 10 ** 3) / (10 ** 3)

    # BMIを元に「肥満度」を表す文字列を返す 
    def get_obestity(self, bmi) -> str:
        result = ""

        if bmi < 18.5:
            result = "低体重（やせ型）"
        elif bmi >= 18.5 and bmi < 25.0:
            result = "普通体重"
        elif bmi >= 25.0 and bmi < 30.0:
            result = "肥満（１度）"
        elif bmi >= 30.0 and bmi < 35.0:
            result = "肥満（２度）"
        elif bmi >= 35.0 and bmi < 40.0:
            result = "肥満（３度）"
        elif bmi >= 40.0:
            result = "肥満（４度）"

        return result 

    # 身長から適正体重を計算し返すメソッドの定義
    def get_suitable_weight(self) -> float:
        # 適正体重 = 身長（m単位）の2乗 × 22
        suitable_weight = (Person.__height/100) ** 2 * 22
        return math.floor(suitable_weight * 10 ** 3) / (10 ** 3)

# Personクラスのインスタンス生成 
person = Person("鈴木一朗", 42, "男性", 179.3, 72.7)

# 個人情報を表示  
person.disp_info()

# BMI値を表示
bmi = person.get_bmi()
print("BMI値 = {}".format(bmi))

# 肥満度を表示
print("肥満度判定 = {}".format(person.get_obestity(bmi))) 

# 適正体重を表示
print('適正体重 = {} kg'.format(person.get_suitable_weight()))
