
# 抽象クラスで使用するモジュールをインポート
from abc import *

# 抽象クラスはABCクラスを継承
class Command(ABC):#クラス名
    @abstractmethod#デコレーターを使用して中小メソッドを定義
    def run(self, text):
        pass#処理はなし



'''
抽象クラスは、継承し、ほかのクラスを定義しなければ
インスタンス化ができない
'''

