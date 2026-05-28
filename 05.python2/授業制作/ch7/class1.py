'''
マングリングで属性を外部から隠ぺいする
'''

# Pokemonクラスを定義
class Pokemon:
    # 属性(クラス共通)
    # インスタンス化したポケモンのカウント
    count = 0

    # 初期化メソッド
    # レベルと番号を受け取り、自分自身のレベルと名前に設定
    def __init__(self, level, name):
        #    ↓ アンダーバーを追加したらメイン側から変更できないようにする
        self.__level = level
        self.naem = name
        # インスタンス化のカウント
        Pokemon.count += 1
    
    # メソッド(関数をイメージ)
    # レベルと名前を表示
    def show(self):
        print(Pokemon.count, self.__level, self.naem)
    # レベルを１加算
    def levelup(self):
        self.__level += 1


# Pokemonクラスをインスタンス化(実体化)
# 変数名 = クラス名()
hitokage = Pokemon(5, 'ヒトカゲ')
# showメソッドを呼び出し
# ヒトカゲのshow
hitokage.show()

hitokage.levelup()
hitokage.show()

# ゼニガメのインスタンス化
zenigame = Pokemon(4, 'ゼニガメ')
# ゼニガメのshow
zenigame.show()