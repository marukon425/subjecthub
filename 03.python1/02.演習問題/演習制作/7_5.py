'''
 While文とcontinue文を用いて1から100までの数字のうち、3の倍数以外の数字を画面に表示するプログラ
ムを作成しなさい。 
 
【実行結果】 
1  
2  
4  
5  
… 
100
'''
# 初期設定
num = 0

# 繰り返し
while num < 100:
    num += 1
    if num % 3 == 0:
        continue
    print (num)
