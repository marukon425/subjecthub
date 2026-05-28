'''
国語の得点>>>
算数の得点>>>
社会の得点>>>
英語の得点>>>
合計得点:
平均得点:
'''
# 空の得点リストを作成
score = []
# 国語の得点リストを入力 (整数化に注意)
score.append (int (input ("国語の得点を入力")))
'''
別解
ja = int (input ("国語の得点を入力"))
score.append (ja)
'''
# 国語の得点リストを入力
score.append (int (input ("算数の得点を入力")))
# 社会の得点リストを入力
score.append (int (input ("社会の得点を入力")))
# 英語の得点リストを入力
score.append (int (input ("英語の得点を入力")))

# 合計を計算
print(f"合計得点は{sum(score)}")

# 平均を計算
print(f"平均得点は{ sum(score) / len(score)}")