import math

# 空欄を表す文字列 -  
BRANK = "-"

class Game:
    # プレイヤー１のお名前 A
    PLAYER_NAME1 = "A"
    # プレイヤー２のお名前 B
    PLAYER_NAME2 = "B"

    # ○×ゲームのフィールドを表す2重配列(3×3)
    # BRANKで初期化しておく
    fields = [[BRANK for j in range(3)] for i in range(3)]

    # 先攻のターンなのか、後攻のターンなのかを管理する
    # true = 先攻、false = 後攻
    turn = True

    # startメソッド
    # ○×ゲームを開始から終了までコントロールするメソッド
    def start(self) -> None:
        # 無限ループ　1ループ=1ターン
        # 必ずゲームが終了する(breakする)ようになっているので、無限ループでも問題なし
        # 現場では危険性の高い無限ループはほぼ使われない。
        # ○×ゲームの場合は9ターンまでしかないのは明白なので、for文で9回ループ　推奨
        while True:

            # 現状の表示
            print("★ 現在の表★")
            self.display()

            # 入力メソッドを呼び出す
            self.input()

            # ゲームが終了しているか確認するisEndメソッドを呼び出し、返却値で判定
            if self.is_end():
                # trueが返却された場合はゲーム終了、最後の盤面を表示し無限ループから抜け出す
                self.display()
                break
            else:
                # falseが返却された場合はゲーム続行、手番を入れ替えてループのはじめに戻る
                self.turn = not self.turn

    # 座標の入力を行うメソッド
    def input(self) -> None:
        # 入力値を管理する変数inputX,inputY
        inputX = 0
        inputY = 0
        # 不正な値を検出した時に表示するメッセージの文字列 msg
        msg = ""

        # 正しい値が入力されるまで繰り返す
        while True:
            # 入力を促す文字列を出力(横軸)
            # 先攻なら先攻プレイヤー名を、後攻なら後攻プレイヤー名を表示する
            print("先攻：" + self.PLAYER_NAME1 if self.turn else "後攻：" + self.PLAYER_NAME2, end="")
            # 入力(横軸)
            inputX = int(input("さんの横(x)座標を入力："))
            
            # 入力を促す文字列を出力(縦軸)
            # 先攻なら先攻プレイヤー名を、後攻なら後攻プレイヤー名を表示する
            print("先攻：" + self.PLAYER_NAME1 if self.turn else "後攻：" + self.PLAYER_NAME2, end="")
            # 入力(縦軸)
            inputY = int(input("さんの縦(y)座標を入力："))

            # 入力された値が正しいかチェックするcheckInputメソッドを呼び出す
            # 戻り値は表示するべき文字列:String 正しい値が入力されていた場合は空文字
            msg = self.check_input(inputY, inputX)

            # msgの中身が空文字の場合は正しい値なのでループから抜け出す
            if len(msg) == 0:
                break
            else:
                # 空文字でない場合はメッセージを表示してループの始めに戻る Line.73
                print(msg)

        # 無限ループを抜け出してきた、すなわち正しい値が入力されているのでターンプレイヤーの名前を指定された座標に入力
        self.fields[inputY][inputX] = self.PLAYER_NAME1 if self.turn else self.PLAYER_NAME2


    # 引数で送られてきた座標が正しい値かどうかチェックする
    # 重複や存在しない座標が入力された場合は入力し直すように呼びかける文字列を返却する
    def check_input(self, y: int, x: int) -> str:
        # 返却用文字列 空文字として初期化
        # 重複や存在しない座標が入力された場合は入力し直すように呼びかける文字列セットする
        msg = ""

        # 座標が0~2の範囲内かどうか判定
        if 0 <= y and y <= 2 and 0 <= x and x <= 2:
            # 座標が0~2の場合、空欄かどうかチェックする
            if not self.is_brank(self.fields[y][x]):
                # 座標が空欄でなかった場合、msgに "まだ埋まっていない座標を入力して下さい。" をセットする
                msg = "まだ埋まっていない座標を入力して下さい。"
            # 座標が0~2で空欄の場合は正しい値なので、空文字のままにする
        else:
            # 座標が0~2の範囲内でない場合、msgに "座標は0~2までの整数で入力してください。" をセットする
            msg = "座標は0~2までの整数で入力してください。"

        # msgを返却する
        return msg

    # ゲームの終了条件を満たしているかチェックし、終了する場合には終了処理をするメソッド
    # ゲームの終了条件(いずれかのプレイヤーが1列そろえているor全てマスが埋まっている)を満たしていればtrueを、満たしていなければfalseを返却する
    def is_end(self) -> bool:
        # 返却用の変数 flg falseで初期化しておく
        flg = False
        # 先攻のプレイヤーが勝っているかどうかの判定
        # フィールド上の縦横斜めのいずれかがそろっていれば勝利
        if self.is_victory(self.PLAYER_NAME1):
            # 先攻プレイヤーが勝利している場合
            # 勝利メッセージを表示
            print("★★ " + self.PLAYER_NAME1 + "さんの勝利★★")
            # 返却用のflgにtrueを代入する
            flg = True

        # 後攻のプレイヤーが勝っているかどうかの判定
        # フィールド上の縦横斜めのいずれかがそろっていれば勝利
        elif self.is_victory(self.PLAYER_NAME2):
            # 後攻プレイヤーが勝利している場合
            # 勝利メッセージを表示
            print("★★ " + self.PLAYER_NAME2 + "さんの勝利★★")
            # 返却用のflgにtrueを代入する
            flg = True

        # 盤面がすべて埋まっているかどうかの判定をするisFillメソッドを呼び出し判定
        elif self.is_full():
            # どちらのプレイヤーも勝利しておらず、
            # 全てのマスが埋まっている場合は引き分け
            # 引き分けメッセージを表示
            print("★★ 引き分け★★")
            # 返却用のflgにtrueを代入する
            flg = True

        # flgを返却する。いずれかの終了条件を満たしていればtrue、そうでなければfalse。
        return flg


    # 現在の盤面を表示をする
    def display(self) -> None:
        # フィールドの座標案内(横軸)
        print("  0 1 2")
        print("  -----")
        # 2重ループを使って、配列を平面上に描画する
        # 外のループは行(縦軸)のループ　1周 = 1行
        for j in range(3): 
            # フィールドの座標案内(縦軸)
            print(str(j) + "|", end="")
            # 内のループは列(横軸)のループ　1周 = 1マス
            for k in range(0, 3):
                # フィールドの状態を1マスずつ描画(改行なし)
                print(self.fields[j][k] + " ", end="")
            # 改行
            print()

    # 引数がBRANKと等しいかチェック
    def is_brank(self, s: str) -> bool :
        return s == BRANK

    # isFullメソッド
    # 引数：　なし　戻り値：flg:boolean
    # 盤面が全て埋まっているかどうかチェック
    # 全て埋まっていればtrueを、埋まっていなければfalseを返却
    def is_full(self) -> bool:
        # 返却用変数flg trueで初期化
        flg = True
        # fieldsを2重ループで走査
        for i in range(3):
            for j in range(3):
                # 全てのマスを確認し、BRANKのマスがあればflgにflaseを代入する
                if self.is_brank(self.fields[i][j]):
                    flg = False
        return flg

    # isVictoryメソッド
    # 引数：　String:playerName　戻り値： boolean:flg
    # 引数で送られてきたプレイヤーが勝利条件を満たしているかチェック
    # 勝利条件を満たしていた場合はtrueを、満たしていなければfalseを返却する
    def is_victory(self, playerName:str) -> bool:
        # 返却用変数flg flaseで初期化
        flg = False

        # 勝利条件を満たしているかどうか判定する
        # 縦、横、斜めのうち1列でもそろっていれば勝利
        if ((self.fields[0][0] == playerName and self.fields[0][1] == playerName and self.fields[0][2] == playerName)   # 縦1列目
         or (self.fields[1][0] == playerName and self.fields[1][1] == playerName and self.fields[1][2] == playerName)   # 縦2列目
         or (self.fields[2][0] == playerName and self.fields[2][1] == playerName and self.fields[2][2] == playerName)   # 縦3列目
         or (self.fields[0][0] == playerName and self.fields[1][0] == playerName and self.fields[2][0] == playerName)   # 横1列目
         or (self.fields[0][1] == playerName and self.fields[1][1] == playerName and self.fields[2][1] == playerName)   # 横2列目
         or (self.fields[0][2] == playerName and self.fields[1][2] == playerName and self.fields[2][2] == playerName)   # 横3列目
         or (self.fields[0][0] == playerName and self.fields[1][1] == playerName and self.fields[2][2] == playerName)   # 斜め1列目
         or (self.fields[0][2] == playerName and self.fields[1][1] == playerName and self.fields[2][0] == playerName)): # 斜め2列目
            # 勝利条件を満たしている場合、trueを代入する
            flg = True

        # 判定結果を返却
        return flg

# メイン処理
game = Game()
game.start()
