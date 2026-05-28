# Animalスーパークラスを作る
class Animal:
    # 初期化
    def __init__(self,name):
        self.name = name
    
    def move(self, length):
        print(f'{self.name}は{length}メートル走りました')
    
# 犬クラス
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def move(self, length):
        print(f'{self.name}は{length}メートル走りました')

# 鳥クラス
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def move(self, length):
        print(f'{self.name}は{length}メートル飛びました')

# クジラクラス
class Whale(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def move(self, length):
        print(f'{self.name}は{length}キロメートル泳ぎました')

# メイン
dog = Dog('犬')
dog.move(10)
bird = Bird('鳥')
bird.move(1000)
whale = Whale('鯨')
whale.move(50)
