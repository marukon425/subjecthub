# クラス===================================================

class stu:
    def __init__(self, name, food):
        self.name = name
        self.food = food
    
    def show(self):
        print(f'名前：{self.name}')
        print(f'好きな食べ物：{self.food}')


class ITstu(stu):
    def __init__(self, name, food, typing):
        super().__init__(name, food)
        self.typing = typing

    def show(self):
        super().show()
        print(f'タイピング文字数：{self.typing}')


class BKstu(stu):
    def __init__(self, name, food, boki):
        super().__init__(name, food)
        self.boki = boki
    
    def show(self):
        super().show()
        print(f'簿記の得点：{self.boki}')

# クラス===================================================


# メイン===================================================
mee1 = ITstu('丸山', '梨', 99999999)
mee1.show()
mee2 = BKstu('新和', 'お茶', 13)
mee2.show()