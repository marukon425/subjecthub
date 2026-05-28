'''
「Hello」を10回画面に表示する
関数(メソッド)を定義し、実行するプログラムを作成しなさい。
'''

#######　関数　#######
# 関数名：reuturn
# 処理内容:同じ内容の物を10回繰り返し表示
# 戻り値:a
def return_print(a):
    for i in range(10):
        print(a)
    return a

return_print("hello")
