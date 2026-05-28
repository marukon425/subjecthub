# 左下が直角の三角形を描画
print("直角三角形を描画します。")
print("2～20までの整数値を入力して下さい。")
bottom = int(input("底辺の長さを入力："))

if bottom < 2 or bottom > 20:
    print("値が正しくありません。")
else:
    # 直角三角形の描画
    for i in range(bottom):
        for j in range(i + 1):
            print("*", end="")
        print()
