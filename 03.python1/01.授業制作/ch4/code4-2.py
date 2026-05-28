# 凝り返し(while文)の学習
'''
【while文の書き方】
while 繰り返し条件:
    繰り返す処理

※繰り返す条件⇒この条件の間繰り返す
'''


# 羊が3まで数える　3回まで 数える

# カウントするために変数(count)を初期化 (これをしないと動かない)
count = 0
# count が 3未満の間 繰り返す
while count < 3 :
    # 繰り返す処理(countを1増加、羊の数匹匹表示)
    count += 1
    print (f"羊が{count}匹")

    count += 1
    print (f"羊が{count}匹")

    count += 1
    print (f"羊が{count}匹")


print("おやすみなさい")