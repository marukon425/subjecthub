# 戻り値が複数ある場合
'''
return文が返却できる値は「1つ」しかない
タプル(リストの変更不可にできる関数)によるアンパック代入
'''
#####関数#####
# 二つの値を受け取り、加算・減算の結果を返す
def plus_and_minus(a, b):
    plus = a + b
    minus = a - b
    return plus, minus #戻り値は１つが原則
#####メイン#####
# 2つの値を送る
# ２つの値が返却される(アンパック代入)
main_plus, main_minus = plus_and_minus(100, 20)

print (main_plus, main_minus)