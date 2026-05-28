# リストの要素を降順に並び替えて表示する

# 整数値リスト
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# 削除したい要素のインデックス番号を入力
while True:
    print("整数値リスト：", array)
    index = int(input("削除する要素のインデックス番号を入力してください。"))
    # インデックス番号が領域外
    if index >= len(array) or index < 0:
        print("インデックス番号が不正です。再入力してください。")
        print()
    else:
        break

# 指定されたインデックス番号の要素を削除
array.pop(index)

# 削除実行後のリストの全要素を表示
print("削除後の整数値リスト =", array)
