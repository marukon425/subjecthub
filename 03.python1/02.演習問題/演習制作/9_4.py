'''
整数の引数を 1 つ受け取って 3 倍にして返す関数(メソッド)を定義しなさい。その関数(メソッド)を利用し
て、ユーザが入力した整数の9倍の数を以下の実行例を参考に画面に表示するプログラムを作成しなさい。 
【実行例】 
整数を入力してください：6 
6 の9倍は54です。 
'''
######### 関数　#########
# 関数名：3_double
# 処理内容：受け取った数値を３倍にして返す
# 引数：double　※三倍にして返す元データ
# 戻り値：result　※三倍にしたデータ

def double_three(double):
    # 引数を三倍にする
    result = double*3
    # 三倍にした数値を表示
    print (result)
    # 結果をメインへ ※return文
    return result

########　メイン　########
doubre1 = int(input("整数を入力してください"))
# 関数を呼び出して、結果を受け取る
double_result = double_three(doubre1) #3倍
double_result = double_three(double_result) #９倍
# 結果を表示
print(f"{doubre1}の9倍は{double_result}です")

