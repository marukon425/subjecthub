'''
開始数、終了数を入力後、開始数から終了数までを全て合計し、計算結果を画面に表示するプログラムを作成
しなさい。 
【実行例】 
開始数：30 
終了数：100 
合 計：4615
'''
start_num = int(input("開始数"))
end_num = int(input("終了数"))
total = 0

for i in range(start_num, end_num+1):
    total += i
print(total)