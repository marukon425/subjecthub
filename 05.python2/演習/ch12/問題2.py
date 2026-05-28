# Personを作る
class Person:

    # 初期化メソット
    def __init__(self, name, job):
        self.name = name
        self.job = job
    
    # introduceメソッドを作る
    def introduce(self):
        print(f'氏名：{self.name}')
        print(f'職業：{self.job}')
    

    
# Teacherサブクラスを作る
class Teacher(Person):
    def __init__(self, name, job, subject):
        super().__init__(name, job)
        self.subject = subject
    
    def introduce(self):
        super().introduce()
        print(f'担当教科：{self.subject}')

# Cookクラスを作る
class Cook(Person):
    def __init__(self, name, job, food):
        super().__init__(name, job)
        self.food = food
    
    def introduce(self):
        super().introduce()
        print(f'得意料理：{self.food}')

# メイン
a = Teacher('近藤勇', '教員', 'Go 言語')
a.introduce()
b = Cook('沖田総司', 'シェフ', 'オムライス')
b.introduce()