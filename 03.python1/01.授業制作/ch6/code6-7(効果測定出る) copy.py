###### オブジェクトのidentity (管理用番号)

# リストオブジェクトの２つ作成
scores1 = list((80, 40, 50))
scores2 = list((80, 40, 50))

# scores1 と 2 を表示
print(scores1, scores2)

# scores1 と 2 をidentity (管理番号) 表示 コピー前
print(f"scores1をidentity (管理番号) 表示:{id(scores1)}")
print(f"scores2をidentity (管理番号) 表示:{id(scores2)}")

# scores2の中身をscores1にコピー
print("scores2の【中身ではなく保存先】をscores1にコピー")
scores1 = scores2
# 【オブジェクトのコピー】
# 中身のコピーではなく、保存先(管理番号)のコピー

# scores1の先頭を90に書き換え
print("scores1の先頭を90に書き換え")
print("scores1を変更すると、保存先が同じscores2も変更される")
scores1[0] = 90

# scores1と2を表示
print(scores1, scores2) # ⇐scores2はscores1に代入されてるため、scores2も90が代入されてる

# scores1 と 2 をidentity (管理番号) コピー後を表示 ※ idが同じなってる
print(f"scores1をidentity (管理番号) 表示:{id(scores1)}")
print(f"scores2をidentity (管理番号) 表示:{id(scores2)}")
