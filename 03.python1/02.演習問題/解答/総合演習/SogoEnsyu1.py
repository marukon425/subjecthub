import random

# CPUとじゃんけんを行うクラス
# 勝敗の結果と連勝した数を表示する
class CoordinationExercise:
    hands = ["グー", "チョキ", "パー"]
    retry = -1
    winCnt = 0

    while True:
        user = -1
        # 乱数でCPUの出し手を取得
        cpu = random.randint(0, 2)

        while True:
            # ユーザ入力用のメッセージ表示
            print("「じゃんけんポン！」")
            for i in range(3):
                print("({}){}　".format(i, hands[i]))
            
            user = int(input("："))

            print("user=", user)

            # 0か1か2以外はもう１度入力
            if user >= 0 and user <= 2:
                break
        
        # 両者の手を表示
        print("私は{}で、あなたは{}です。\n".format(hands[cpu], hands[user]))

        # 勝敗の判定
        judge = (cpu - user + 3) % 3

        if judge == 0:
            print("引き分けです。")
        elif judge == 1:
            print("あなたの勝ちです。")
            winCnt += 1
        elif judge == 2:
            print("あなたの負けです。")

        retry = 0
        while True:
            print("連勝は{}でした。\n".format(winCnt))

            # 負けた場合は連勝数をクリア
            if judge == 2:
                winCnt = 0

            retry = int(input("もう１度勝負しますか？ (0)いいえ　(1)はい："))
            # 0か1以外はもう１度入力
            if retry == 0 or retry == 1:
                break
    
        # 0の場合は終了。1の場合はもう１度じゃんけんする
        if retry == 0:
            break
