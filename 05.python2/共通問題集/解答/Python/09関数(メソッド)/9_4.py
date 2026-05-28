def triple(num):
    """ 引数に指定された値を3倍にして返却する """
    
    return num*3

# メイン処理
input_num = int(input("整数を入力してください："))

# 3倍する関数（メソッド）の呼び出し
triple_num = triple(input_num)
# さらに3倍する
ninetimes_num = triple(triple_num)

# 画面表示
print(input_num, "の9倍は", ninetimes_num, "です。", sep="")
