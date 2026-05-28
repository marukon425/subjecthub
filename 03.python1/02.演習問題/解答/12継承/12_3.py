class Animal:
    """ 動物クラス """

    def __init__(self, name: str) -> None:
        """ コンストラクタ """
        self.name = name

    def move(self, length: int) -> None:
        """ 移動 """
        print("{}は、{}メートル動きました。".format(self.name, length))

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
        print("{}は、{}キロメートル泳ぎました。".format(self.name, length))

# 犬クラス作成
dog = Dog("犬")
# 鳥クラス作成
bird = Bird("鳥")
# 鯨クラス
whale = Whale("鯨")

# 移動したメッセージを表示
dog.move(10)
bird.move(1000)
whale.move(50)
