# 作成した連想配列の値を表示

# 連想配列を作成
vegetable_dict = {"野菜　　" : "季節",
                  "キャベツ" : "春",
                  "スイカ　" : "夏",
                  "ナス　　" : "秋",
                  "ハクサイ" : "冬"}

# 連想配列の全要素を表示
for key,value in vegetable_dict.items():
    # タイトルと季節が春のものだけ表示
    if value == "季節" or value == "春":
        print(key, "：", value, sep="")
