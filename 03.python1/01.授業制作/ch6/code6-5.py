# クラス(設計図)からオブジェクトを生成

# クラス(設計図)を作成
class Pokemon:
    #### データ
    name = ""          # 名前:
    hp = 0             # ＨＰ
    attack_power = 0   # 攻撃力

    ########### メソッド(処理) ###########
    # 初期値を設定するメソッド
    def __init__(self, name, hp, attack_power):
        # 受け取ったデータを自分のデータに代入
        self.name = name
        self.hp = hp
        self.attack_power = attack_power

    # 名前とhpと攻撃力を表示するメソッド 引数・戻り値なし
    def show(self):
        print(f"名前：{self.name}")
        print(f"HP：{self.hp}")
        print(f"攻撃力：{self.attack_power}")

    # 攻撃(attack)のメソッド  ○○が△△攻撃(改行)敵は逃げた(改行)
    def attack(self):
        print(f"{self.name}が{self.attack_power}攻撃")
        print("敵は逃げた")

########### メインプログラム ###########

# クラス(クラス) を使用して、オブジェクトを作成
pika = Pokemon('ピカチュウ', 100, 20)
pika.show()
pika.attack()
print("----------------------------------------------------------------------------")
riorase = Pokemon('リオレイス', 500, 1000)
riorase.show
riorase.attack
print("----------------------------------------------------------------------------")
pocha = Pokemon('ポッチャマ', 20, 100)
pocha.show()
pocha.attack()


