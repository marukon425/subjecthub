# 整数を10回入力させ合計値を表示する
# ただし0が入力されたら繰り返し処理終了
sum = 0

for i in range(1, 11):
    num = int(input(str(i) + "回目の入力："))
    # 0入力判定
    if num == 0:
        print("0が入力されました。")
        break

    # 入力値を合算
    sum += num
    
# 合計値を表示
print("合計：", sum, sep="")
