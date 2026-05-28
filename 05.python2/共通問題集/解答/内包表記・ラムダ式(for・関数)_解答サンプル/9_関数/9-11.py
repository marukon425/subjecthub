# 1～4の乱数を発生させ結果を表示
import random as rd

""" 1～4の乱数を発生させ返却する """
get_fortune = lambda:rd.randint(1, 4)

# メイン処理

# 運勢を取得する関数（メソッド）の呼び出しと結果表示
result = get_fortune()
if result == 1:
    print("本日の運勢：絶好調")
elif result == 2:
    print("本日の運勢：好調")
elif result == 3:
    print("本日の運勢：不調")
elif result == 4:
    print("本日の運勢：絶不調")
