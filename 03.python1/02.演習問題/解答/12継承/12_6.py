class Book:
    """ 書籍クラス """

    # インスタンス生成数管理カウンター
    __counter = 0

    @staticmethod
    def get_count() -> int:
        """ 現在のカウント数を取得 """
        return Book.__counter

    # コンストラクタ
    def __init__(self, title: str, author: str, price: int) -> None:
        # 著名
        self.title = title
        # 著者名
        self.author = author
        # 出版年
        self.price = price
        # カウンターを更新
        Book.__counter += 1
        # 識別番号を設定
        self.id = Book.get_count()
    
    # 書籍情報を表示
    def display_info(self) -> str:
        print("書名：{}".format(self.title))
        print("著者名：{}".format(self.author))
        print("価格：{}".format(self.price))
        print("識別番号：{}".format(self.id))

class PaperBook(Book):
    """ 紙書籍クラス """

    def __init__(self, title: str, author: str, price: int, page_number: int) -> None:
        """ コンストラクタ """
        super().__init__(title, author, price)
        self.page_number = page_number
    
    # 書籍情報を表示
    def display_info(self) -> None:
        print("書名：{}".format(self.title))
        print("著者名：{}".format(self.author))
        print("価格：{}円".format(self.price))
        print("識別番号：{}".format(self.id))
        print("ページ数：{}ページ".format(self.page_number))

class EBook(Book):
    """ 電子書籍クラス """

    def __init__(self, title: str, author: str, price: int, file_size: int) -> None:
        """ コンストラクタ """
        super().__init__(title, author, price)
        self.file_size = file_size
    
    # 書籍情報を表示
    def display_info(self) -> None:
        print("書名：{}".format(self.title))
        print("著者名：{}".format(self.author))
        print("価格：{}円".format(self.price))
        print("識別番号：{}".format(self.id))
        print("ファイルサイズ：{}KB".format(self.file_size))
    
# 書籍情報を作成
paper_book1 = PaperBook("吾輩は猫である", "夏目漱石", 850, 245)
paper_book2 = PaperBook("ノルウェイの森", "村上春樹", 1200, 328)
e_book1 = EBook("Python入門", "Python.org", 2400, 9824)
e_book2 = EBook("Web技術の仕組み", "www.org", 4530, 12458)

# 書籍情報を表示
paper_book1.display_info()
print()
paper_book2.display_info()
print()
e_book1.display_info()
print()
e_book2.display_info()
print()
# 現在の識別番号を取得して表示
print("与えた識別番号 ＝ {}個".format(Book.get_count()))
