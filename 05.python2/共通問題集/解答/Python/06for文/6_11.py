# 指定されたサイズの長方形を描画
print("長方形を描画します。")
print("2～20までの整数値を入力して下さい。")

row_num = int(input("行数の入力："))
if row_num < 2 or row_num > 20:
    print("値が正しくありません。")
else:
    col_num = int(input("列数の入力："))
    if col_num < 2 or col_num > 20:
        print("値が正しくありません。")
    else:
        # 長方形の描画
        for i in range(1, row_num+1):
            for j in range(col_num):
                print("*", end="")
            print()
