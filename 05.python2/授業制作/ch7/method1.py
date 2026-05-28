'''
クラスの作り方
'''

# Pokemonクラスを定義
class Pokemon:
    # 属性　番号と名前

    # 初期化メソッド
    # レベルと番号を受け取り、自分自身のレベルと名前に設定
    def __init__(self, level, name):
        self.level = level
        self.naem = name
    
    # メソッド(関数をイメージ)
    # レベルと名前を表示
    def show(self):
        print(self.level, self.naem)

# Pokemonクラスをインスタンス化(実体化)
# 変数名 = クラス名()
hitokage = Pokemon(100, 'ヒトカゲ')

# showメソッドを呼び出し
# ヒトカゲのshow
hitokage.show()

# ゼニガメのインスタンス化
zenigame = Pokemon(200, 'ゼニガメ')
# ゼニガメのshow
zenigame.show()