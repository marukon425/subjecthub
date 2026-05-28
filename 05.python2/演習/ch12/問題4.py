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
    
    def food(self, food):
        print(f'{self.name}はお肉を食べました')

# 鳥クラス
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def move(self, length):
        print(f'{self.name}は{length}メートル飛びました')

    def food(self, food):
        print(f'{self.name}は虫を食べました')
# クジラクラス
class Whale(Animal):
    def __init__(self, name):
        super().__init__(name)
    
    def move(self, length):
        print(f'{self.name}は{length}キロメートル泳ぎました')

    def food(self, food):
        print(f'{self.name}はオキアミを食べました')
# メイン
dog = Dog('犬')
dog.move(10)
bird = Bird('鳥')
bird.move(1000)
whale = Whale('鯨')
whale.move(50)
