'''
 整数の引数を2つ受け取って足し算をする関数(メソッド)と、同様に引き算、掛け算、割り算、余り算をする
関数(メソッド)を定義しなさい。それらの関数(メソッド)を利用してユーザが入力した2つの整数の足し算、引
き算、掛け算、割り算、余り算の結果を以下の実行例を参考に画面に表示するプログラムを作成しなさい。 
 
【実行例】 
整数を入力してください：7 
整数を入力してください：3 
7+3=10 
7-3=4 
7*3=21 
7/3=2 
7%3=1
'''
####### 関数 ########
# 関数名：calculation
# 処理内容：整数の引数を2つ受け取って足し算、引き算、掛け算、割り算、余り算をする
# 引数：a, b
# 戻り値：result
def calculation(a, b) :
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = int(a / b)
    remainder_calculation = a % b
    result = f"{a}+{b}={addition}\n{a}-{b}={subtraction}\n{a}*{b}={multiplication}\n{a}/{b}={division}\n{a}%{b}={remainder_calculation}"
    print(result)
    return result




########メイン########
calculation(7, 3)
