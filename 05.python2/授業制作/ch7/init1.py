'''
クラスの作り方
'''

# Foodクラスを定義
# class クラス名
class Pokemon:
    # 属性　番号と名前

    # 初期化メソッド
    # 名前と番号を受け取り、自分自身の番号と名前に設定
    def __init__(self, no, name):
        self.no = no
        self.naem = name
    
    # メソッド

# Pokemonクラスをインスタンス化(実体化)
# 変数名 = クラス名()
hitokage = Pokemon(100, 'ヒトカゲ')

# hitokageオブジェクトに属性を設定
# hitokage.name = 'ヒトカゲ'
# print(hitokage.name, hitokage.no)

print(hitokage.naem, hitokage.no)


# ゼニガメのインスタンス化
zenigame = Pokemon(200, 'ゼニガメ')
print(zenigame.naem, zenigame.no)