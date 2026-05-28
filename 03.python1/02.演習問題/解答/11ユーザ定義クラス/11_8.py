class Person:
    """ 個人情報クラス """ 
 
    # コンストラクタ
    def __init__(self, name: str, age: int, address: str, mail: str) -> None:
        self.status = "正常"
        self.set_name(name)
        self.set_age(age)
        self.set_address(address)
        self.set_mail(mail)

    # 名前を設定
    def set_name(self, name: str) -> None:
        self.name = name

    # 年齢を設定
    def set_age(self, age: int) -> None:
        self.age = age

        # 年齢の範囲チェック
        if self.is_valid_age(age) == False:
            # 年齢の許容範囲外のためステータスに異常を設定
            self.status = "異常"
    
    # 住所を設定
    def set_address(self, address: str) -> None:
        self.address = address

    # メールアドレスを設定
    def set_mail(self, mail: str) -> None:
        self.mail = mail

        # 年齢の範囲チェック
        if self.is_valid_mail(mail) == False:
            # 不正なメールアドレスのためステータスに異常を設定
            self.status = "異常"

    # 年齢の範囲チェック
    def is_valid_age(self, age: int) -> bool:
        result = True
        if age < 0 or age > 99:
            # 年齢の許容範囲外のためステータスに異常を設定
            result = False
        
        return result
    
    # メールアドレスのチェック
    def is_valid_mail(self, mail: str) -> bool:
        result = True

        # アドレスに@を含んでいるかチェック
        if mail.find("@") <= 0:
            # @が含まれない、または先頭に@があるため不正
            result = False
        
        return result

    # 個人情報を表示
    def disp_info(self):
        print("{}さん  {}歳  {}  {}  {}".format(self.name, self.age, self.address, self.mail, self.status))

# Personクラスのインスタンス生成 
person_a = Person("A", 18, "千代田区神田神保町1-1", "aaa@mail.com")
person_b = Person("B", -3, "横浜市西区桜木町2-2-2", "bbb@mail.com")
person_c = Person("C", 20, "さいたま市北区大原3-3", "@email.co.jp")

# 個人情報を表示
person_a.disp_info()
person_b.disp_info()
person_c.disp_info()
