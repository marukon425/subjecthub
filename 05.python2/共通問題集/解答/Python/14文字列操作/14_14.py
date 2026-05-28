# 入力した住所の市または郡または区のみを表示

# 市郡区比較用の配列
comp_list = []

# 住所を2つ入力してもらう
for i in range(1, 3):
    address_str = input(str(i) + "つ目の住所を入力：")

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

    # 市郡区の最終文字のインデックス番号を取得
    end_index = 0
    if address_str.find("市") != -1:
        end_index = address_str.find("市")
    elif address_str.find("郡") != -1:
        end_index = address_str.find("郡")
    else:
        end_index = address_str.find("区")

    # 市または郡または区を格納
    comp_list.append(address_str[start_index+1:end_index+1])

# 市郡区を比較して結果を表示
if comp_list[0] == comp_list[1]:
    print("同じ", comp_list[0][-1], "ですね。ご近所さんです。", sep="")
else:
    print("同じ", comp_list[0][-1], "ではないようです。", sep="")
