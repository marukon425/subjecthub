# 入力した住所の都道府県以下の住所を表示

address_str = input("住所を入力してください：")

#都道府県名の最終文字のインデックス番号を取得
index = 0
if address_str.find("東京都") != -1:
    index = address_str.find("都")
elif address_str.find("北海道") != -1:
    index = address_str.find("道")
elif address_str.find("大阪府") != -1 or address_str.find("京都府") != -1:
    index = address_str.find("府")
elif address_str.find("県") != -1:
    index = address_str.find("県")

# 都道府県以下の住所を表示
print(address_str[index+1:])
