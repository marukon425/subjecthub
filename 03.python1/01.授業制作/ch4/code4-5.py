'''
【while文の書き方】
while 繰り返し条件:
    繰り返す処理

※繰り返す条件⇒この条件の間繰り返す
'''

# キーボードから入力された人数の得点集計、平均点の表示

# ===初期設定 (繰り返し前)===
# キーボードから人数を入力
student_num = int(input("人数を入力>>>"))
# 人数をカウントする変数の初期化
count = 0
# リスト変数(score)の初期化 ※空リスト
score_list = []

# ===繰り返す処理　カウント が入力された人数 未満の間===
while count < student_num:
    # 人数カウントの更新(加算) 
    count += 1
    # 得点リストに入力された得点を追加 (apend)
    score_list.append (int(input("得点を追加>>>"))) 

# ===繰り返し後の処理===
# リストの表示
print(score_list)

# 平均点の計算 (合計 ÷ 個数)
# 合計⇒　sum(リスト変数名)
# 個数⇒ キーボードから入力された人数　またはlen(リスト変数名)
print(f"合計平均は{sum(score_list) / len(score_list)}")