# 1から100を表示するプログラム

# カウントを初期化する
count = 0
while count < 100 :
    count += 1 # ⇐これがないと無限ループする
    print(count)

# 別解
count1 = 0

# count
count1 = 1
while count < 100 :
    count1 += 1
    print(count1)


# ============1から100を足すプログラム============

# カウントする変数の初期化
count2 = 1

# 合計する変数の初期化 (基本0)
toal = 0

# 1～100まで合計を繰り返す
while count2 < 101 :
    # 繰り返す処理(合計にカウントを加算、カウントの更新)
    toal += count2  # 合計にカウントを加算
    '''print("おやすみなさい")
    注釈
    totla = total + count2 totalは箱だからcountが加算されたものがどんどん入っていく
    '''
    count2 += 1  # カウントに1を加算

# 合計を表示
print (toal)



