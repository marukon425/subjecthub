# 巻子の引数と【戻り値】の学習
'''
戻り値とは、呼び出し元に返す値

return変数名
'''

###### 関数
#関数名；add
# 処理：引数を加算answerに代入し、結果を呼び出しもとに返す
# 引数：num1, num2
# 戻り値：amswer
def add(num1, num2):     #筆記数:num1, num2
    answer = num1 + num2 # 引数を加算しanswerに代入
    return answer        #結果を呼び出しもとに返す

###### メイン
# 10, 20 を引数として、add関数を呼び出し、結果をmain_answerに代入
main_answer = add(10, 20)
# main_answerを表示
print(f"足し算結果は{main_answer}")

# 結果は表示されるが、結果は格納されてない
print(f"足し算結果{add(30,100)}")





