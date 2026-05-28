import math

def disp_ave(score_dict):
    """ 引数に指定された連想配列の値から平均点を表示する """
    sub1_sum = 0
    sub2_sum = 0
    sub3_sum = 0

    for name, score_array in score_dict.items():
        person_sum = 0

        # 各科目の得点を取得
        index = 0
        for score in score_array:
            # 個人の合計得点に加算
            person_sum += score
            
            # 科目ごとの合計得点に加算
            if index == 0:
                sub1_sum += score
            elif index == 1:
                sub2_sum += score
            elif index == 2:
                sub3_sum += score

            # インデックス番号を追加
            index += 1
        
        # 個人の平均点を表示
        person_ave = person_sum / len(score_array)
        print(name + "さんの平均点は", math.floor(person_ave * 10 ** 2) / (10 ** 2), "点です。", sep="")
    
    # 科目ごとの平均点を表示
    sub_ave = sub1_sum / len(score_dict)
    print("1教科目の平均点は", math.floor(sub_ave * 10 ** 2) / (10 ** 2), "点です。", sep="")
    sub_ave = sub2_sum / len(score_dict)
    print("2教科目の平均点は", math.floor(sub_ave * 10 ** 2) / (10 ** 2), "点です。", sep="")
    sub_ave = sub3_sum / len(score_dict)
    print("3教科目の平均点は", math.floor(sub_ave * 10 ** 2) / (10 ** 2), "点です。", sep="")

# メイン処理

# 個人の3科目の点数を保持する連想配列
info_dict = {}
# 何人目かを特定する番号
no = 1

while True:
    name = input(str(no) + "人目の名前を入力して下さい：")
    # end が入力されたら終了
    if name == "end":
        break

    score1 = int(input(str(no) + "人目の1教科目の点数を入力して下さい："))
    score2 = int(input(str(no) + "人目の2教科目の点数を入力して下さい："))
    score3 = int(input(str(no) + "人目の3教科目の点数を入力して下さい："))
    info_dict[name] = [score1, score2, score3]

    no += 1

# 平均点を表示する関数
disp_ave(info_dict)
