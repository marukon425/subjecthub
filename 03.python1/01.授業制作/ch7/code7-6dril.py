import random

count_hit = 0
game_count = 0
continu  = 0

game_flag = True
# フラグを立てる
while game_flag == True:
    # ヒットが３だった場合プログラムを終了
    # game_countを初期化
    if count_hit == 3:
        game_count = 0
        answer.clear
        prediction.clear
        break
    # 違った場合
    else:
        # geme_countが1だった場合、コンティニューするか聞く※0だったら飛ばす
        if game_count == 1:
            continu = input("ゲームを続け増すか？１：続ける ２：終了>>>")
        elif continu == 2:
                break
        else:
            # 3つランダムな数値を格納する
            game_count += 1
            print('数当てゲームを始めます。3桁の数を当ててください！')
            answer = []
            for i in range(3):
                answer.append(random.randint(0,9))
            print(answer)
            # 桁を入力
            prediction = []
            for i in range(3):
                prediction.append(int(input(f'{i+1}桁目の予想を入力')))
            print(prediction)
            # ヒットを計算
            count_hit = 0
            for i in range(3):
                if answer[i] == prediction[i]:
                    count_hit += 1
            # ボールを計算
            count_ball = 0
            for i in range(3):
                if str(answer) in str(prediction[i]):
                    count_ball += 1
            # 答え合わせ
            print(f"{count_hit}ヒット！{count_ball}ボール！")
            print('正解です！')