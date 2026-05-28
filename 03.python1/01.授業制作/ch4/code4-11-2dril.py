'''
for文とcontinue文を使用
1～50までを表示
偶数は表示しない(数値を表示せずに先頭に戻る)
'''

for num in range (1, 51) :
    # 偶数の場合は、先頭に戻る
    if num % 2 == 0:
        continue
    # 数値を表示
    print(num)