class BookInfo:
    """ 書籍クラス """

    # 書籍番号
    __book_no = 0

    # コンストラクタ
    def __init__(self, title: str, author: str, year: int) -> None:
        # 書名
        self.set_title(title)
        # 著者名
        self.set_author(author)
        # 出版年
        self.set_year(year)
        # 書籍番号を更新して設定
        BookInfo.__book_no += 1
        self.set_book_no(BookInfo.__book_no)
    
    # 書名を取得
    def get_title(self) -> str:
        return self.name
    
    # 著者名を取得
    def get_author(self) -> str:
        return self.author

    # 出版年を取得
    def get_year(self) -> int:
        return self.year
    
    # 書籍番号を取得
    def get_book_no(self) -> int:
        return self.book_no

    # 書名を設定
    def set_title(self, name: str) -> None:
        self.name = name

    # 著者名を設定
    def set_author(self, author: str) -> None:
        self.author = author

    # 出版年を設定
    def set_year(self, year: int) -> None:
        self.year = year

    # 書籍番号を設定
    def set_book_no(self, book_no: int) -> None:
        self.book_no = book_no
    
# 書籍情報を格納する配列
book_list = []
book_list.append(BookInfo("三国志", "吉川英治", 1989))
book_list.append(BookInfo("楊令伝", "北方謙三", 2011))
book_list.append(BookInfo("竜馬がゆく", "司馬遼太郎", 1998))
book_list.append(BookInfo("坊っちゃん", "夏目漱石", 1906))
book_list.append(BookInfo("吾輩は猫である", "夏目漱石", 1905))

# 書籍情報を表示
for book in book_list:
    print("書    名：{}".format(book.get_title()))
    print("著 者 名：{}".format(book.get_author()))
    print("出 版 年：{}".format(book.get_year()))
    print("書籍番号：{}".format(book.get_book_no()))
