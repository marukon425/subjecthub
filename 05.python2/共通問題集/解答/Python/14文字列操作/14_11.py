# 入力した住所により結果を切り替えて表示

address_str = input("住所を入力してください：")

if address_str.count("市") > 0:
    print("市")
elif address_str.count("郡") :
    print("郡")
else:
    print("東京23区")
