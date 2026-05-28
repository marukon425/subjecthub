'''以下の実行例を参考に、キーボードから文字列1と文字列2を順番に入力し「文字列2」→「文字列」の順で
結合して画面に表示するプログラムを作成しなさい。 
【実行例】 
文字列1:ABCDE 
文字列2:VWXYZ 
VWXYZABCDE 
'''

# char1にABCDEを設定
char1 = "ABCDE"
# char２にVWXYZを設定
char2 ="VWXYZ"
# VWXYZABCDE を出力
print(f"{char2}{char1}")