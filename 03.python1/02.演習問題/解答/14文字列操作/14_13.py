# 入力した住所の市または郡または区のみを表示

address_str = input("住所を入力してください：")

#都道府県名の最終文字のインデックス番号を取得
start_index = 0
if address_str.find("東京都") != -1:
    start_index = address_str.find("都")
elif address_str.find("北海道") != -1:
    start_index = address_str.find("道")
elif address_str.find("大阪府") != -1 or address_str.find("京都府") != -1:
    start_index = address_str.find("府")
elif address_str.find("県") != -1:
    start_index = address_str.find("県")

end_index = 0
if address_str.find("市") != -1:
    end_index = address_str.find("市")
elif address_str.find("郡") != -1:
    end_index = address_str.find("郡")
else:
    end_index = address_str.find("区")

# 都道府県以下の住所を表示
print(address_str[start_index+1:end_index+1])
