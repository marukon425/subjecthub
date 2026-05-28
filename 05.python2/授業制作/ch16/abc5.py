from abc import *

# 抽象クラス(継承)
class Command(ABC):
    @abstractmethod
    def run(self, text):
        pass

# コマンド抽象クラスを継承
class Append(Command):
    def __init__(self, text):
        self.text = text

    def run(self, text):
        return text+self.text

# コマンド抽象クラスを継承
class Insert(Command):
    def __init__(self, index, text):
        self.index = index
        self.text = text
    
    def run(self, text):
        i = self.index
        return text[:i]+self.text+text[i:]
# Commandクラスをインスタンス化

c = [Append('th'), Insert(0, 'py'), Append('on')]
# [Appendクラスのインスタンス化, Insertクラスのインスタンス化, Appendクラスのインスタンス化]
s = ''
# cに一つずつ入れて
for x in c:
    # runメソッドに入れる
    s = x.run(s)
# runメソッドを使い終わったら出力
print(s)
# インスタンス化