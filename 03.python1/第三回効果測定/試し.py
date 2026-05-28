'''
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(input())

y = []
name = []
for i in range(m):
    y_, n_ = input().split()
    y_ = int(y_)
    y.append(y_)
    name.append(n_)

for i in range(len(y)):
    for j in range(0, n - i - 1):
        if y[j] > y[j + 1]:
            # 要素を交換
                y[j], y[j + 1] = y[j + 1], y[j]
                name[j], name[j + 1] = name[j + 1], name[j]

# 答え
N, K = map(int, input().split())
names = [input() for _ in range(N)]

histories = [None] * K
for i in range(K):
    year, charge = input().split()
    histories[i] = (int(year), charge)

for year, name in sorted(histories):
    print(name)
'''

'''
# 入力: 会社数と取引の回数
num_companies, num_transactions = map(int, input().split())

# 各会社のデータを保存する辞書（キー: 会社名, 値: (暗証番号, 残高)）
company_data = {}

# 各会社の情報を受け取る
for _ in range(num_companies):
    company_name, pin_code, balance = input().split()
    company_data[company_name] = (pin_code, int(balance))

# 取引を処理
for _ in range(num_transactions):
    called_company, said_pin, withdraw_amount = input().split()
    withdraw_amount = int(withdraw_amount)

    correct_pin, current_balance = company_data[called_company]

    if said_pin == correct_pin:
        # 正しい暗証番号なら残高から引き出す
        company_data[called_company] = (correct_pin, current_balance - withdraw_amount)
    # 暗証番号が違う場合は何もしない

# 最後に各会社の残高を出力
for company_name in company_data:
    pin_code, final_balance = company_data[company_name]
    print(company_name, final_balance)
'''
# n, m = map(int, input().split())
# bank_account = {}
# for i in range(n):
#     acount, pin, balance = input().split()
#     balance = int(balance)
#     bank_account[acount] = (pin, balance)

# for i in range(m):
#     inp_acount, inp_pin, inp_balance = input().split()
#     inp_balance = int(inp_balance)
#     if bank_account[inp_acount][1] == inp_pin:
#         bank_account[inp_acount][2] = bank_account[inp_acount][2] - inp_balance
# print(bank_account)
# for bank_account in bank_account:
#     print(f'{bank_account}')

# n = input()
# for i in n.split():
#     print(i)

# std_in = input()

# for string in std_in.split():
#     print(string)


# n = int(input())
# dic = {}
# for i in range(n):
#     info = input().split()
#     if info[0] in dic:
#         info[2] = int(info[2])
#         dic[info[0]] += info[2]
#     else:
#         if info[1] == 'join':
#             dic[info[0]] = 0
#         elif info[1] == 'give':
#             info[2] = int(info[2])
#             dic[info[0]] = info[2]

# zero_lst = []

# # print(dic)
# for key, value in list(dic.items()):
#     if value == 0:
#         zero_lst.append(key)
#         del dic[key]

# # print(dic)

# zero_lst.sort()

# sorted_dict = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

# for key, value in sorted_dict.items():
#     print(key)
# for i in range(len(zero_lst)):
#     print(zero_lst[i])


# name1, name2 = input().split()
# combo1 = name1 + name2
# combo2 = name2 + name1
# nums1 = []
# for i in combo1:
#     s = ord(combo1)
#     nums1.append(s)

# # 名前を入力
# name1, name2 = input().split()
# # 結合パターンを2種類作成
# combo1 = name1 + name2
# combo2 = name2 + name1

# # アルファベットを数値に変換（a=1, b=2, ..., z=26）
# nums1 = []
# for c in combo1:
#     c = c.lower()
#     if c.isalpha():
#         nums1.append(ord(c) - ord('a') + 1)

# nums2 = []
# for c in combo2:
#     c = c.lower()
#     if c.isalpha():
#         nums2.append(ord(c) - ord('a') + 1)

# # 数列を縮めて1つの数字にする（隣同士の足し算）
# while len(nums1) > 1:
#     temp = []
#     for i in range(len(nums1) - 1):
#         s = nums1[i] + nums1[i + 1]
#         if s > 101:
#             s -= 101
#         temp.append(s)
#     nums1 = temp

# while len(nums2) > 1:
#     temp = []
#     for i in range(len(nums2) - 1):
#         s = nums2[i] + nums2[i + 1]
#         if s > 101:
#             s -= 101
#         temp.append(s)
#     nums2 = temp

# # 最終スコアを比較して出力
# score1 = nums1[0]
# score2 = nums2[0]

# print(f"{max(score1, score2)}")
'''
class Student:
    def avg(self, math, english):
        print((math + english)/2)
a001 = Student()
a001.avg(30,70)  
'''

# n = int(input())
# num_lst = []
# name_lst = []
# for i in range(n):
#     entry = input().split()
#     if entry[0] == 'make':
#         num_lst.append(entry[1])
#         name_lst.append(entry[2])
#     elif entry[0] == 'getnum':
#         entry[1] = int(entry[1])
#         print(num_lst[entry[1] - 1])
#     elif entry[0] == 'getname':
#         entry[1] = int(entry[1])
#         print(name_lst[entry[1] - 1])
#     elif entry[0] == 'change_num':
#         entry[1] = int(entry[1])
#         num_lst[entry[1] - 1] = entry[2]
#     elif entry[0] == 'change_name':
#         entry[1] = int(entry[1])
#         name_lst[entry[1] - 1] = entry[2]


# values = input().split()
# N = float(values[0])
# M = int(values[1])

# print("{:.{}f}".format(N, M))

# a = int(input())
# for i in range(a):
#     n = input()
#     if len(n) == 3:
#         print(n)
#     elif len(n) == 2:
#         print(f' {n}')
#     else:
#         print(f'  {n}')



# for i in range(1, 10):
#     for j in range(1, 10):
#         print("{: >2}".format(i * j), end="")
#         if j == 9:
#             print()
#         else:
#             print(end=" | ")

#     if i < 9:
#         print("=" * (2 * 9 + 3 * (9 - 1)))


'''
しりとりゲーム
・n人の順番で周回
・発言はk個の単語からしか発言できない
・今まで使われた単語は使ったらいけない
・zで終わる単語を発言したらダメ
・あとは普通のしりとりと同じルール
ルールを破ったらその人は除外

最終的に残ってる人の番号を出力
'''
'''
失敗
# n = 何人か　k = 何個かの単語　m = 何回かの発言
n, k, m = map(int, input().split())

# 参加者をまとめる
participant_lst = []
for i in range(n):
    participant_lst.append(i + 1)

#単語のリストの作成 
word_lst = []
for i in range(k):
    word_lst.append(input())

count = 0
for i in range(m):
    # 何回周回したか数える
    count += 1
    # 初期の単語を作成
    befo_word = input()
    if befo_word in word_lst:
        count += 1
        now_word = input()
        # 入力された単語があるあか検索
        if now_word in word_lst:
            # あった場合
                # 前の単語の末尾と今の文字の先頭が同じか調べる
            if befo_word[-1] == now_word[0]:
                # 同じ場合
                befo_word = now_word
            else:
                
                if count > len(participant_lst):
                    dropout = (count % len(participant_lst)) -1
                else:
                    participant_lst.pop(count-1)

        else:
            # なかった場合
            # 脱落
            if count > len(participant_lst):
                dropout = (count % len(participant_lst)) -1
            else:
                participant_lst.pop(count-1)

    # 違った単語を入力した場合
    else:
        # カウントが参加者リストの合計を上回ってたら
        if count > len(participant_lst):
            dropout = (count % len(participant_lst)) -1
        else:
            participant_lst.pop(count-1)

for i in participant_lst:
    print(i)
'''

# values = input().split()
# H = int(values[0])
# W = int(values[1])
# A = int(values[2])
# B = int(values[3])

# for i in range(H):
#     for j in range(W):
#         print("({}, {})".format(A, B), end="")
#         if j == W - 1:
#             print()
#         else:
#             print(end=" | ")

#     if i < H - 1:
#         print("=" * (6 * W + 3 * (W - 1)))



# n, q = map(int, input().split())
# a = input().split()
# for i in range(q):
#     s = input().split()
#     if len(s) == 2:
#         s[1] = int(s[1])
#     if s[0] == '0':
#         a.append(s[1])
#     elif s[0] == '1':
#         del a[-1]
#     else:
#         for i in range(len(a)):
#             if i + 1 < len(a):
#                 print(a[i], end=' ')
#             else:
#                 print(a[i])

# 座標
# H, W, r, c = map(int, input().split())
# coordinate = []
# for i in range(H):
#     coordinate.append(input())

# if coordinate[r-1][c-1] == '#':
#     print('Yes')
# else:
#     print('No')


# '''
# rolling = LLLRB
# upper   = DDRRA
# rush    = AAAAA
# '''
# s = input()
# for i in range(len(s)):
#     print(f'比較：{s[i : i+5]}')
#     if s[i : i+5] == 'LLLRB':
#         print('rolling')
#     elif s[i : i+5] == 'DDRRA':
#         print('upper')
#     elif s[i : i+5] == 'AAAAA':
#         print('rush')

RED = '\033[31m'
END = '\033[0m'

# # 座標のっ問題
# H, W  = map(int, input().split())
# # 座標を格納するリスト
# coordinate = []
# for i in range(H):
#     coordinate.append(input())

# y, x = input().split()
# y = int(y)
# x = int(x)
# # リストに変換して文字列を変更する
# coordinate[y] = list(coordinate[y])
# if coordinate[y][x] == '.':
#     coordinate[y][x] =RED + '#' + END
# else:
#     coordinate[y][x] =RED + '.' + END
# coordinate[y] = ''.join(coordinate[y])
# for i in coordinate:
#     print(i)

'''
# 与えられた座標の書き換え＆周りの上下左右の座標の書き換え
H, W = map(int, input().split())
# 座標の二次元配列
mp = []
for i in range(H):
    mp.append(input())

# 書き換える座標の指定
Y, X = map(int, input().split())

# 文字の書き換えのために一旦二次元配列にする
mp_co = []
for i in range(len(mp)):
    mp_co.append(list(mp[i]))

#1.指定した座標の書き換え
if mp_co[Y][X] == '#':
    mp_co[Y][X] = '.'
elif mp_co[Y][X] == '.':
    mp_co[Y][X] = '#'

# 2.上下左右の書き換え
# 上
# 上の列が存在してるか確かめる
if Y == 0:
    pass
else:
    if mp_co[Y-1][X] == '#':
        mp_co[Y-1][X] = '.'
    elif mp_co[Y-1][X] == '.':
        mp_co[Y-1][X] = '#'
# 下
if Y == len(mp_co):
    pass
else:
    if mp_co[Y+1][X] == '#':
        mp_co[Y+1][X] = '.'
    elif mp_co[Y+1][X] == '.':
        mp_co[Y+1][X] = '#'
# 右
if X == W:
    pass
else:
    if mp_co[Y][X + 1] == '#':
        mp_co[Y][X + 1] = '.'
    elif mp_co[Y][X + 1] == '.':
        mp_co[Y][X + 1] = '#'
# 左
if X == 0:
    pass
else:
    if mp_co[Y][X - 1] == '#':
        mp_co[Y][X - 1] = '.'
    elif mp_co[Y][X - 1] == '.':
        mp_co[Y][X - 1] = '#'

# 戻す
for i in range(len(mp_co)):
    mp_co[i] = ''.join(mp_co[i])
for i in mp_co:
    print(i)
'''


# 与えられた座標の書き換え＆周りの上下左右の座標の書き換え
'''
H, W = map(int, input().split())
# 座標の二次元配列
mp = []
for i in range(H):
    mp.append(input())

# 書き換える座標の指定
Y, X = map(int, input().split())

# 文字の書き換えのために一旦二次元配列にする
mp_co = []
for i in range(len(mp)):
    mp_co.append(list(mp[i]))

#1.指定した座標の書き換え
if mp_co[Y][X] == '#':
    mp_co[Y][X] = RED + '.' + END
elif mp_co[Y][X] == '.':
    mp_co[Y][X] = RED + '#' + END

# 2.上下左右の書き換え
# 上
# 上の列が存在してるか確かめる
if Y == 0:
    pass
else:
    if mp_co[Y-1][X] == '#':
        mp_co[Y-1][X] = RED + '.' + END
    elif mp_co[Y-1][X] == '.':
        mp_co[Y-1][X] = RED + '#' + END
# 下
'''
# if Y == len(mp_co):
#     pass
# else:
#     if mp_co[Y+1][X] == '#':
#         mp_co[Y+1][X] = RED + '.' + END
#     elif mp_co[Y+1][X] == '.':
#         mp_co[Y+1][X] = RED + '#' + END
'''
if Y + 1 < H:
    if mp_co[Y+1][X] == '#':
        mp_co[Y+1][X] = RED + '.' + END
    elif mp_co[Y+1][X] == '.':
        mp_co[Y+1][X] = RED + '#' + END
# 右
if X + 1 < W:
    if mp_co[Y][X + 1] == '#':
        mp_co[Y][X + 1] = RED + '.' + END
    elif mp_co[Y][X + 1] == '.':
        mp_co[Y][X + 1] = RED + '#' + END
'''
# if X == W:
#     pass
# else:
#     if mp_co[Y][X + 1] == '#':
#         mp_co[Y][X + 1] = RED + '.' + END
#     elif mp_co[Y][X + 1] == '.':
#         mp_co[Y][X + 1] = RED + '#' + END
'''
# 左
if X == 0:
    pass
else:
    if mp_co[Y][X - 1] == '#':
        mp_co[Y][X - 1] = RED + '.' + END
    elif mp_co[Y][X - 1] == '.':
        mp_co[Y][X - 1] = RED + '#' + END

# 戻す
for i in range(len(mp_co)):
    mp_co[i] = ''.join(mp_co[i])
for i in mp_co:
    print(i)
'''

# paiza Bランクレベルアップメニュー
# # 指定された座標の全方位斜め方向の塗り替え
# # 座標の範囲の指定
# H, W = map(int, input().split())
# # 座標の二次元配列の初期化
# mp = []
# # 座標の情報を入れていく「#」か「.」で表現
# for i in range(H):
#     mp.append(list(input()))

# # 塗り替えの起点となる座標の入力
# Y, X = map(int, input().split())
# Y = Y - 1
# X = X - 1

# # 起点の座標の塗り替え
# # ※座標の絶対座標は1,1じゃなくて0,0 ←これマジ重要
# if mp[Y][X] == '#':
#     mp[Y][X] = RED+'.'+END
# elif mp[Y][X] == '.':
#     mp[Y][X] = RED+'#'+END


# # 塗り替える座標を指定する変数の初期化
# Y_repaint = Y 
# X_repaint = X 
# # 左上斜め方向の塗り替え
# while True:
#     # 座標の上限位置に来てないか
#     if Y_repaint == 0 or X_repaint == 0:
#         # 上限に来たら繰り返し終了
#         break
#     else:
#         # 起点からどんどん左上斜め方向にずらす
#         Y_repaint = Y_repaint - 1
#         X_repaint = X_repaint - 1
#         # 塗り替える
#         if mp[Y_repaint][X_repaint] == '#':
#             mp[Y_repaint][X_repaint] = RED+'.'+END
#         elif mp[Y_repaint][X_repaint] == '.':
#             mp[Y_repaint][X_repaint] = RED+'#'+END
# Y_repaint = Y
# X_repaint = X
# count = 0
# # 左上斜め方向の塗り替え
# while True:
#     count += 1
#     Y_repaint = Y_repaint - 1
#     X_repaint = X_repaint + 1
#     # 座標の上限位置に来てないか
#     if Y_repaint == H or X_repaint == W:
#         # 上限に来たら繰り返し終了
#         print('左上斜め方向終了:',count)
#         break
#     else:
#         # 起点からどんどん左上斜め方向にずらす
#         print(count,'周目'+'塗り替えY：',Y_repaint)
#         print('      '+'塗り替えX：',X_repaint)
#         # 塗り替える
#         if mp[Y_repaint][X_repaint] == '#':
#             mp[Y_repaint][X_repaint] = RED+'.'+END
#         elif mp[Y_repaint][X_repaint] == '.':
#             mp[Y_repaint][X_repaint] = RED+'#'+END

# # 塗り替えた座標を出力
# for i in mp:
#     print('after'+''.join(i))

# paiza Bランクレベルアップ　反復横跳び
# N, X, K = map(int, input().split())
# 反復横跳びが中央→右→中央→左→中央→右→中央→左→中央...といった周期4のループであることに注意.
# 線を遠ざけてから,中央→左→中央と移動する回数は(K-4*N)÷4の商と等しい.
# これは周期4のループであり,線を遠ざけてから何ループこなしたかが分かるためである.
# 上に含まれず,線を遠ざけてから,中央→左と移動する回数(左を跨いで反復横跳びが終わる場合)は(K-4*N)÷4の余りが3である時だけ1回加算すればいい.
# print(2*X*((K-4*N)//4)+X*(((K-4*N) % 4)//3))

# 色づけの関数
def coloring(char):
    return RED + char + END
'''
# 座標　(斜め方向)
H, W = input().split()
H = int(H)
W = int(W)
mp = []
# 座標の情報を入力
for i in range(H):
    mp.append(list(input()))
# 反転の起点の情報をを入力
Y, X = map(int, input().split())

# 反転の関数
def reverse(Y, X):
    if mp[Y][X] == '#':
        mp[Y][X] = coloring('.')
    elif mp[Y][X] == '.':
        mp[Y][X] = coloring('#')

# 起点の反転
reverse(Y, X)

# 上下左右の反転
# 上下
for i in range(H):
    reverse(i, X)
# 左右
for i in range(H):
    reverse(Y, i)
# 斜め方向の反転
# 右下斜め方向の反転
count = 0
while True:
    count += 1
    reverse_Y = count + Y
    reverse_X = count + X
    # 反転できる上限に来てないか確かめる
    if reverse_Y < H or reverse_X < W:
        reverse(reverse_Y, reverse_X)
        for i in mp:
            print(''.join(i))
        print('='*len(mp[0]))
    else:
        count = 0
        break
# 左上斜め方向
while True:
    count += 1
    reverse_Y = Y - count
    reverse_X = X - count
    # 反転できる上限に来てないか確かめる
    if reverse_Y >= 0 or reverse_X >= 0:
        reverse(reverse_Y, reverse_X)
        for i in mp:
            print(''.join(i))
        print('='*len(mp[0]))

    else:
        count = 0
        break
# 右上斜め方向
while True:
    count += 1
    reverse_Y = Y - count
    reverse_X = X + count
    # 反転できる上限に来てないか確かめる
    if reverse_Y <= 0 or reverse_X >= W:
        count = 0
        break
    else:
        reverse(reverse_Y, reverse_X)
        for i in mp:
            print(''.join(i))
        print('='*len(mp[0]))

# 左下斜め方向
while True:
    count += 1
    reverse_Y = Y + count
    reverse_X = X - count
    # 反転できる上限に来てないか確かめる
    if reverse_Y >= H or reverse_X <= 0:
        count = 0
        break
    else:
        reverse(reverse_Y, reverse_X)
        for i in mp:
            print(''.join(i))
        print('='*len(mp[0]))

# 出力
for i in mp:
    print(''.join(i))
'''

'''
マップのナンバリング

'''

H, W, D = map(int, input().split())
mp = []
mp_sb = []
# 方向が横向きの場合
count = 0
if D == 2:
    for i in range(H):
        for j in range(W):
            count += 1
            mp_sb.append(count)
        mp.append(mp_sb)
        mp_sb.clear

print(mp)