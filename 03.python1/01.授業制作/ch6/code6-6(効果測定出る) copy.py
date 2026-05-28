###### オブジェクトのidentity (管理用番号)

# リストオブジェクトの２つ作成
scores1 = list((80, 40, 50))
scores2 = list((80, 40, 50))

# scores1 と 2 を表示
print(scores1, scores2)
# scores1 と 2 をidentity (管理番号) 表示
print(f"scores1をidentity (管理番号) 表示:{id(scores1)}")
print(f"scores2をidentity (管理番号) 表示:{id(scores2)}")
