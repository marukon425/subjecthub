# 繰り返し(while文)の復習
'''
1つめの数字
2つめの数字
3つめの数字
4つめの数字
合計は〇〇です、平均は〇〇です
'''

# ===========初期設定===========
# 何回入力するか分からない⇒フラグを立てる
is_end = True
# 数字を入れるリストを作る
num_list = []
# 〇〇目を表示するカウントを初期化
count = 0

# ===========繰り返し===========
while is_end ==True  :
    count += 1
    num_list.append (int(input(f"{count}目の数字を入力")))
    a = input ("まだ入力しますか？")
    if a == "n":
        # noだったらfalseにして繰り返し終了
        is_end = False

# ===========繰り返し後===========
# 合計・平均を表示                          ↓ 少数点を省く
print (f"合計は{sum(num_list)}です。平均は{int(sum(num_list)/len(num_list))}です")


