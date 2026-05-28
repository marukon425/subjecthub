# 指定された件数分個人情報を連想配列に格納し表示する

info_dict = {}

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
