
# リスト変数scoreに 88, 95, 90, 70　を設定
score = [88, 95, 90, 70]

# 関数(機能)を使用して合計を計算
total = sum(score)

# totalを表示(〇点)
print(f"合計{total}点")

# 変数ave　に平均を計算
# ave = total/3
# 要素数を出す関数(機能)　　len(リスト関数)リストが何個あるか数えてくれる
ave = total / len(score)

# 合計と平均を表示
print(f"平均点は{ave}点")
# print(f"合計点は{ave}")

# 追加前のリストを表示
print(f"追加前：{score}")

# リストに追加　リスト変数名.apend(追加する要素)
# score に　60を追加
score.append (60)

# 追加後のリストを表示
print (f"追加後{score}")

# リストの削除　リスト変数名.remove(追加する要素)
# score.remove (60)
score.remove (60)

# score　から　90 を削除
score.remove (90)

# 削除後のリストを表示
print (f"削除後：{score}")

# スライス表記　( リスト変数名［A:B］) A以上B未満
# scoreの１以上３未満(１と２)を表示
print (f"添え字が１以上３未満：{score[1:3]}")
