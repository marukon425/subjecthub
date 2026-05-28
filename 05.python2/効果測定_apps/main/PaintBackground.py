from paint import Paint
# ターミナルに色を付けて出力する派生クラス(背景に色を付ける)
class PaintBackground(Paint):
    def black(self,text):
        return '\033[40m'+text+'\033[0m'
    def red(self,text):
        return '\033[41m'+text+'\033[0m'
    def green(self,text):
        return '\033[42m'+text+'\033[0m'
    def yellow(self,text):
        return '\033[43m'+text+'\033[0m'
    def blue(self,text):
        return '\033[44m'+text+'\033[0m'
    def magenda(self,text):
        return '\033[45m'+text+'\033[0m'
    def cyan(self,text):
        return '\033[46m'+text+'\033[0m'
    def white(self,text):
        return '\033[47m'+text+'\033[0m'

