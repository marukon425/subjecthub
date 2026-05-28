import random

class Coincase:
    """ コインケースクラス """ 
 
    # コンストラクタ
    def __init__(self) -> None:
        # 硬貨の種類ごとの枚数を保持する辞書を作成
        self.coins = {1:0, 5:0, 10:0, 50:0, 100:0, 500:0}

    # typeで指定された硬貨をcountで指定された枚数分追加
    def add_coin(self, type: int, count: int) -> None:
        self.coins[type] += count

    # typeで指定された硬貨の枚数を返却
    def get_coin_count(self, type: int) -> int:
        return self.coins[type]

    # 全硬貨の総額を返却
    def get_amount(self) -> int:
        total = 0

        for type, count in self.coins.items():
            total += type * count

        return total

# Coincaseクラスのインスタンス生成 
coincase = Coincase()

# ランダムに硬貨を追加
for _ in range(10):
    num = random.randint(1, 6)
    if num == 1:
        coincase.add_coin(1, 1)
    elif num == 2:
        coincase.add_coin(5, 1)
    elif num == 3:
        coincase.add_coin(10, 1)
    elif num == 4:
        coincase.add_coin(50, 1)
    elif num == 5:
        coincase.add_coin(100, 1)
    elif num == 6:
        coincase.add_coin(500, 1)

# 個人情報を表示
print("1円：{}枚  5円：{}枚  10円：{}枚  50円：{}枚  100円：{}枚  500円：{}枚".format(
        coincase.get_coin_count(1), coincase.get_coin_count(5), coincase.get_coin_count(10), 
        coincase.get_coin_count(50), coincase.get_coin_count(100), coincase.get_coin_count(500)))
print("総額：{:,}円".format(coincase.get_amount()))
