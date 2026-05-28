# メッセージの表示
print("BMI値を求めます")

# 身長(cm)を入力
cm = float(input("身長(cm)："))
# 体重(Kg)を入力
weight = float(input("体重(Kg)："))

# 身長をメートル換算
height = cm / 100
# BMI値を計算
bmi = weight / (height * height)

# BMI値の表示
print("BMI値 =", bmi)
