'''
メインプログラムで２つの数値を入力
入力した２つの数値を関数を送り、合計を表示する
'''
##################　関数　##################
# 関数名：compute
# 処理内容：num1とnum2の合計を出力
# 引数(受け取る内容)：num_1, num_2
def compute(num1, num2):
    total = num1 + num2
    print(f"合計は{total}")

# 関数名：add() 足し算
# 処理内容：add_num1とadd_num2の合計を出力
# 引数(受け取る内容)：add_num1, add_num2
def add(add_num1, add_num2):
    print(f"合計は{add_num1 + add_num2}です")

# 関数名：sub() 引き算
# 処理内容：sub_num1とsub_num2の引き算を出力
def sub(sub_num1, sub_num2):
    print(f"計算結果は{sub_num1 - sub_num2}です")

# 関数名：mod() 剰余
# 処理内容：mod_num1とmod_num2の引き算を出力
def mod(mod_num1,mod_num2):
    print(f"余りは{mod_num1 % mod_num2}です")


##################　メイン　##################
# num1とnum2をconpite関数に数値を送る
# １つめの数値を入力
num_1 = int(input("１つめの数値を入力"))
# ２つめの数値を入力
num_2 = int(input("２つめの数値を入力"))
# 〇と〇を因数として、〇〇を呼び出し
compute(num_1, num_2)
add(num_1, num_2)
sub(num_1, num_2)
mod(num_1, num_2)

