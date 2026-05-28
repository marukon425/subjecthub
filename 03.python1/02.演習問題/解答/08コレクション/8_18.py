# 商品と在庫数の連想配列の作成から表示
# その後、在庫数を更新して結果を表示

# 連想配列を作成
item_dict = {"A" : 500, "B" : 2030, "C" : 1980}
# 販売数の連想配列を作成
sold_dict = {"A" : 50, "B" : 450, "C" : 460}

print("＜現在の在庫＞")
# 連想配列の全要素の表示
for key,value in item_dict.items():
    print("商品", key, "：", value, "個", sep="")
    # 販売数を反映
    item_dict[key] = value - sold_dict[key]

print("＜販売数反映後の在庫＞")
# 販売数を反映した後の連想配列の全要素の表示
for key,value in item_dict.items():
    print("商品", key, "：", value, "個", sep="")
