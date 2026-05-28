def get_bmi(height, weight):
    """ 引数に指定された身長と体重を元にBMIを算出し返却する """
    # 身長をcmからmに変換して計算
    bmi = weight / ((height/100) * (height/100))
    return bmi

def get_std_weight(height):
    """ 引数に指定された身長を元に適正体重を算出し返却する """
    # 身長をcmからmに変換して計算
    std_weight = ((height/100) * (height/100)) * 22
    return std_weight

# メイン処理

# 身長と体重を入力
height = float(input("身長(cm)を入力してください："))
weight = float(input("体重(㎏)を入力してください："))

# BMIを算出する関数（メソッド）の呼び出しと結果表示
bmi = get_bmi(height, weight)
print("BMI値は", "{:.2f}".format(bmi), "です", sep="")

# 適正体重を算出する関数（メソッド）の呼び出しと結果表示
std_weight = get_std_weight(height)
print("適正体重は", "{:.2f}".format(std_weight), "kgです", sep="")
