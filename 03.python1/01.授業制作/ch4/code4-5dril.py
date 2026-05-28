'''
単語を入力>>>
単語を入力>>>
単語を入力>>>
単語を入力>>>

入力された単語を表示
'''
# ===初期設定===
# リストを初期化
word_list = []
# フラグの初期設定
is_end = True



# ===繰り返し処理===
while is_end == True :
    # 単語を入力
    word_list.append (input("単語を入力>>>"))
    # まだ入力するか聞く
    a = input("まだ入力しますか？")
    # NOだったらフラグをFalse
    if a == "n" :
        is_end = False
# ===繰り返し後の処理===
# リストの表示
print(word_list)





'''
【別解】

# 単語のリストを初期化
word_list2 = list()
# フラグの初期化(True)
is_word2 = True

# 【繰り返し処理】
# フラグがTrueの間繰り返す
while is_word2 == True:
    # 単語を入力
    word2 = input("単語を入力")
    # 単語が end かを判断
    if word2 == "end" :
        # フラグを False に置き換え
        is_word2 = False
    # 単語をリストに追加
    word_list2.append(word2)

# 繰り返し後の処理
# 単語リスト変数を表示
print(word_list2)

'''




