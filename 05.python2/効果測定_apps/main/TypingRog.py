from Typing import Typing
from PaintBackground import PaintBackground
txt_back = PaintBackground()
class TypingRog(Typing):
    
    # 初期メソッドは基底クラスで定義しているため必要なし
    # ユーザー登録(ログイン)するメソッド
    def user(self, username):
        # ログイン処理
        print('ユーザーネームを入力してください')
        while True:
            if username == 'ログイン':
                n = input('>>>')
                if self.db.serch_name(n):
                    print('ログインできました')
                    return n
                else:
                    print('ログインできません\n再度入力してログインしてください')
                    continue
                # 名前だけをuserdataテーブルに保存
                # 名前が存在してるか検索する
            else:
                if self.db.serch_name(username):
                    print('その名前は使われてます。再度入力してください')
                    username = input('>>>')
                    continue
                else:
                    # 存在してない場合
                    # 新規登録
                    # ほかのデータはNULLで保存
                    self.db.reg_name(username)
                    print(txt_back.blue('登録できました'))
                    return username
