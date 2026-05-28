from paint import Paint

class PaintText(Paint):
    def black(self,text):
        return '\033[30m'+text+'\033[0m'
    def red(self,text):
        return '\033[31m'+text+'\033[0m'
    def green(self,text):
        return '\033[32m'+text+'\033[0m'
    def yellow(self,text):
        return '\033[33m'+text+'\033[0m'
    def blue(self,text):
        return '\033[34m'+text+'\033[0m'
    def magenda(self,text):
        return '\033[35m'+text+'\033[0m'
    def cyan(self,text):
        return '\033[36m'+text+'\033[0m'
    def white(self,text):
        return '\033[37m'+text+'\033[0m'