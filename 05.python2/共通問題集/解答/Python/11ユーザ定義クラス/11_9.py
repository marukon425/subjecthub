class Car:
    """ 車クラス """

    # コンストラクタ
    def __init__(self, name: str, maker: str, price: int) -> None:
        # 車名
        self.set_name(name)
        # メーカー名
        self.set_maker(maker)
        # 価格
        self.set_price(price)

    # 車名を取得
    def get_name(self) -> str:
        return self.name
    
    # メーカー名を取得
    def get_maker(self) -> str:
        return self.maker

    # 価格を取得
    def get_price(self) -> int:
        return self.price

    # 車名を設定
    def set_name(self, name: str) -> None:
        self.name = name

    # メーカー名を設定
    def set_maker(self, maker: str) -> None:
        self.maker = maker

    # 価格を設定
    def set_price(self, price: int) -> None:
        self.price = price


# 車情報を格納する配列
car_list = []
car_list.append(Car("RX-7", "MAZDA", 5000000))
car_list.append(Car("RX-8", "MAZDA", 8000000))
car_list.append(Car("GT-R R34", "NISSAN", 10000000))

# 検索キーワード入力
keyword = input("検索するキーワード:")

# 車名かメーカー名にマッチする車情報を検索
is_match = False
for car in car_list:
    if car.get_name() == keyword or car.get_maker() == keyword:
        # 該当する車情報を表示
        print("車名：{}".format(car.get_name()))
        print("メーカー名：{}".format(car.get_maker()))
        print("価格：{}".format(car.get_price()))
        print()

        # 該当する車情報が存在したのでマッチングフラグを更新
        is_match = True

# 検索結果を表示
if is_match == False:
    print("検索結果　0件")
    print("検索条件を変えてください。")
