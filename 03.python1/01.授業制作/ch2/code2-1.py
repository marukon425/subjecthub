'''
【問題点】
1.科目数が増えると変数が増加
2.科目をまとめて処理できない
※上記内容を効率よく管理したい！！
'''

# 変数net,db,sc　に 88,95,90,を設定
net =int(95)
db = int(95)
sc = int(90)

# 変数total　に　3つの合計を集計
total = net + db + sc

# 変数ave　に平均を計算
ave = total/3

# 合計と平均を表示
print(f"合計点は{ave}")



