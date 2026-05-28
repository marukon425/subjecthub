# 初期設定
# フラグをTrueに設定する
score_flag = True
# 合計人数を数えるための変数を初期化
total_count = 0
# 合格者数を数えるための変数を初期化
passing_count = 0

# 繰り返し処理
while score_flag == True:
    # 変数(score)に得点を入力する
    score = (input ("得点を入力してください>>>"))
    # 入力されたものがendだった場合、繰り返し処理を終了
    if score == "end":
        break
    # endじゃない場合
    else :
        # 変数scoreを score_intに文字型から整数型に変換する
        score_int = int (score)
        #合計人数を数える 
        total_count += 1
        # 合格者数を数えるための条件分岐を設定
        if score_int >= 60:
            passing_count += 1
        # それでも違う場合の処理は特に無いのでここで処理終了

# 合格者数は〇人中〇人を表示
print (f"合格者数は{total_count}人中{passing_count}人")

