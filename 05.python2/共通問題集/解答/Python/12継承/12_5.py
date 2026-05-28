# 動物クラスにのみeatメソッドを追加しているのがポイント
# moveメソッドと異なりメッセージが同一なので子クラスにメソッド追加は不要

class Animal:
    """ 動物クラス """

    def __init__(self, name: str) -> None:
        """ コンストラクタ """
        self.name = name

    def move(self, length: int) -> None:
        """ 移動する """
        print("{}は、{}メートル動きました。".format(self.name, length))

    def eat(self, food: str) -> None:
        """ 食事する """
        print("{}は、{}を食べました。".format(self.name, food))

class Dog(Animal):
    """ 犬クラス """

    def __init__(self, name: str) -> None:
        """ コンストラクタ """
        super().__init__(name)

    def move(self, length: int) -> None:
        """ 移動 """
        print("{}は、{}メートル走りました。".format(self.name, length))

class Bird(Animal):
    """ 鳥クラス """

    def __init__(self, name: str) -> None:
        """ コンストラクタ """
        super().__init__(name)

    def move(self, length: int) -> None:
        """ 移動 """
        print("{}は、{}メートル飛びました。".format(self.name, length))

class Whale(Animal):
    """ 鯨クラス """

    def __init__(self, name: str) -> None:
        """ コンストラクタ """
        super().__init__(name)

    def move(self, length: int) -> None:
        """ 移動 """
        print("{}は、{}キロ泳ぎました。".format(self.name, length))

class Human(Animal):
    """ 人間クラス """

    def __init__(self, name: str) -> None:
        """ コンストラクタ """
        super().__init__(name)

    def move(self, length: int) -> None:
        """ 移動 """
        print("{}は、{}メートル歩きました。".format(self.name, length))

# 犬クラス作成
dog = Dog("犬")
# 鳥クラス作成
bird = Bird("鳥")
# 鯨クラス
whale = Whale("鯨")
# 人クラス
human = Human("人")

# 移動と食事のメッセージを表示
dog.move(10)
dog.eat("お肉")
bird.move(1000)
bird.eat("虫")
whale.move(50)
whale.eat("オキアミ")
human.move(300)
human.eat("昼ご飯")
