# 作成した連想配列の値を変更して表示

# 連想配列を作成
info_dict = {"id" : 100, "name" : "大原太郎", "age" : 19}

# キー「age」に該当する値を変更
info_dict["age"] = 20

# 結果を表示
for key,value in info_dict.items():
    print(key, "：", value, sep="")
