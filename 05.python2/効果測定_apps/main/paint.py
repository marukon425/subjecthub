from abc import *
# ターミナルに色を付けて出力するクラス(抽象クラス)
class Paint:
    @abstractmethod
    def black(self,text):
        pass
    @abstractmethod
    def red(self,text):
        pass
    @abstractmethod
    def green(self,text):
        pass
    @abstractmethod
    def yellow(self,text):
        pass
    @abstractmethod
    def blue(self,text):
        pass
    @abstractmethod
    def magenda(self,text):
        pass
    @abstractmethod
    def cyan(self,text):
        pass
    @abstractmethod
    def white(self,text):
        pass
