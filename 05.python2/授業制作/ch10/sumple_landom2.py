# ランダム数値10個のリストを作成　(内報表記を活用)
from random import randint as ri
num_lst = [ri(1,10) for i in range(10)]

# リストを表示
print('ランダム数値10個のリストを作成：',num_lst)

# リストをシャッフル
from random import shuffle as sf
sf(num_lst)

# シャッフルしたリスト
print('シャッフル：',num_lst)

# リストから１つの数値をチョイス
from random import choice as ch
print('数字を一つチョイス',ch(num_lst))
