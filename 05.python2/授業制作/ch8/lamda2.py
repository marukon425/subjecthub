# 関数名：loop
# 引　数：f(sqiare関数　⇒　return ⇒ x*x)
# 戻り値：なし
def loop(f):
    for i in range(10):
        # f(i) ⇒ sqiare関数を呼び出し ⇒ x*x ⇒ i*i
        print(f(i), end= ' ')

# その場で関数を定義(lamda)し、引数として受け取る
# 無名関数：xを受け取りx*xを返す
loop(lambda x: x*x)

