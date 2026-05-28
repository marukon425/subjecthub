# 指定された件数分個人情報を連想配列に格納し表示する
# 平均年齢も合わせて表示する

info_dict = {}
# 入力された全員分の年齢合計値
sum_age = 0

input_num = int(input("入力件数 = "))

for i in range(input_num):
    print(i+1, "件目の個人情報入力", sep="")
    name = input("名前 = ")
    age = int(input("年齢 = "))

    info_dict[name] = age

print()
# 連想配列の全要素の表示
for key,value in info_dict.items():
    print("名前：", key, "、年齢：", value, sep="")
    sum_age += value

# 入力された個人情報が1件以上の場合のみ表示
if len(info_dict) > 0:
    print("平均年齢は", sum_age / len(info_dict), "歳です。", sep="")
