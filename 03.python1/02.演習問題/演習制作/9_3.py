'''
第1引数で指定された文字列を第2引数で指定された回数分表示する関数(メソッド)を定義しなさい。
その関数(メソッド)を利用して以下の実行結果となるように画面に表示するプログラムを作成しなさい。 
【実行結果】 
Hello 
Hello 
Hello 
Good morning 
Good morning 
Good morning 
Good morning 
Good evening 
Good evening
'''

######## 関数 ########
# 関数名：word
# 処理内容：二つの文字列を入出力しそれぞれの文字列を措定回数分出力する
# 引数：word1, word_return
# 戻り値：word1, word_return
def word1(word1, word_return1):
    for i in range(word_return1):
        print(word1)
    return word1, word_return1,

word1("hello", 3)
word1("Good morning ", 3)
word1("Good evening ", 2)
