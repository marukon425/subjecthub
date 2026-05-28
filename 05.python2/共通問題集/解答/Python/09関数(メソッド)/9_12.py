import math

def disp_result(score_dict):
    """ 引数に指定された連想配列の値から合否判定と平均点を表示する """
    sum_score = 0

    for name, score in score_dict.items():
        result = ""
        # 平均点算出のため点数を合算
        sum_score += score

        # 合否判定（60点以上が合格）
        if score >= 60:
            result = "合格"
        else:
            result = "不合格"

        print(name, "さんは", result, "です。" , sep="")

    # 平均点の表示
    ave = sum_score / len(score_dict)
    print("平均点は、", math.floor(ave * 10 ** 2) / (10 ** 2), "です。", sep="")

# メイン処理

info_dict = {}

for i in range(3):
    name = input(str(i+1) + "人目の名前を入力して下さい：")
    score = int(input(str(i+1) + "人目の得点を入力して下さい："))
    info_dict[name] = score

# 合否結果と平均点の表示
disp_result(info_dict)
