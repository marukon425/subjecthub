'''while文を用いて複数の整数を入力し、入力された整数の合計と平均を画面に表示するプログラムを作成しな
さい。ただし”0”が入力されたら入力を終了させ合計と平均を画面に表示するようにしなさい。また負の数が
入力されたら合計と平均に含めないようにしなさい。 

【実行例】 
整数を入力：3 
整数を入力：-1 
整数を入力：4 
整数を入力：1 
整数を入力：0 
合計値：8 
平均値：2 
'''


# 初期設定
# 合計平均をするための空リストを作成
count = 0
num_flag = True
total = 0
count = 0
count2 = 0

# 繰り返し
while num_flag == True:
    num = int(input("整数を入力"))
    
    if num == 0:
        break
    else:
        total += num
        count1 = 1
        if num >=0:
            count +=1

print(f"合計値{total}")
print(f"平均値{total/count1}")
print(f"{count1}個入力されたが、{count-count1}は正常な値が入力された")