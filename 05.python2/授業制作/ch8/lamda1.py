# 関数名：loop
# 引　数：f(sqiare関数　⇒　return ⇒ x*x)
# 戻り値：なし
def loop(f):
    for i in range(10):
        # f(i) ⇒ sqiare関数を呼び出し ⇒ x*x ⇒ i*i
        print(f(i), end= ' ')

# 関数名：sqiare
# 引　数：x
# 戻り値：x*x
def sqiare(x):
    return x*x

# loop関数を呼び出し
# sqiareを呼び出してる

# 処理(x*x)を引数とする場合は、関数定義し引数として設定する必要がある
loop(sqiare)