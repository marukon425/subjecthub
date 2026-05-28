# ===================クラス===================

# studentクラスの定義
class student:
    # ☆　初期化メソッド　☆
    # 名前と好きな食べ物を設定
    def __init__(self, name, food):
        self.name = name
        self.food = food

    # ☆　メソッド　☆
    # 表示
    def show(self):
        print('名前：'+self.name, ' 好きな食べ物：'+self.food)

# ====================メイン====================
# インスタンス化
me = student('丸山', '梨')
# 表示
me.show()

you = student('新和', 'お茶')
you.show()