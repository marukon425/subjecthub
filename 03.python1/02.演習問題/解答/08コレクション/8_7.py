# 1～10を格納したリストを作成し、要素を降順に並び替えて表示する

# 整数値リスト
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# リストの要素を降順に並び替え
sorted_array = sorted(array, reverse=True)

# リストの全要素を表示
for i in sorted_array:
    print(i)
