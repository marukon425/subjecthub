# Bookクラスを作る(スーパークラス)
class Book:

    # カウンターを作る
    count = 0

    def __init__(self, title, auther, price, ):
        Book.count += 1
        self.title = title
        self.auther = auther
        self.price = price
        self.id = Book.count
    
    def getCount(self):
        print(f'書名：{self.title}')
        print(f'著書名：{self.auther}')
        print(f'価格：{self.price}円')
        print(f'識別番号：{self.id}')

# PaperBookクラス(サブクラス)を作る
class PaperBook(Book):
    def __init__(self, title, auther, price, page_num):
        super().__init__(title, auther, price)
        self.page_num = page_num
    
    def getCount(self):
        super().getCount()
        print(f'ページ数{self.page_num}ページ')

# EBook
class EBook(Book):
    def __init__(self, title, auther, price, page_num):
        super().__init__(title, auther, price)
        self.page_num = page_num
    
    def getCount(self):
        super().getCount()
        print(f'ファイルサイズ{self.page_num}KB')


# メイン
wagahai = PaperBook('吾輩は猫である', '夏目漱石', 850, 245)
wagahai.getCount()
nolway = PaperBook('ノルウェイの森', '村上春樹', 1200, 328)
nolway.getCount()
python = EBook('Python', 'Pthon.org', 2400, 9824)
python.getCount()
web = EBook('Web技術の仕組み', 'www.org', 4350, 12458)
web.getCount()

