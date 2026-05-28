# 計算実行と結果の表示

class Person:
    """ 人クラス """

    def __init__(self, name: str, job: str) -> None:
        """ コンストラクタ """
        self.name = name
        self.job = job

    def introduce(self) -> None:
        """ 自己紹介 """        
        print("氏名：{}".format(self.name))
        print("職業：{}".format(self.job))

class Teacher(Person):
    """ 教師クラス """

    def __init__(self, name: str, job: str, subject: str) -> None:
        """ コンストラクタ """
        super().__init__(name, job)
        self.subject = subject

    def introduce(self) -> None:
        """ 自己紹介 """        
        super().introduce()
        print("担当科目：{}".format(self.subject))

class Cook(Person):
    """ 料理人クラス """

    def __init__(self, name: str, job: str, specialities: str) -> None:
        """ コンストラクタ """
        super().__init__(name, job)
        self.specialities = specialities
    
    def introduce(self) -> None:
        """ 自己紹介 """        
        super().introduce()
        print("得意料理：{}".format(self.specialities))

# 教師クラス作成
teacher = Teacher("近藤勇", "教員", "Go言語")
# 料理人クラス作成
cook = Cook("沖田総司", "シェフ", "オムライス")

# 自身の情報を表示
teacher.introduce()
print()
cook.introduce()
