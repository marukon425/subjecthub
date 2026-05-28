# 入力値を降順に並び替えして表示
print("0～100までの得点（整数値）を2つ入力してください")
pt1 = int(input("1つ目の得点："))
pt2 = int(input("2つ目の得点："))

# 同じ得点の場合は得点を1つ表示し、それ以外の場合は得点を降順に２つ表示する
if pt1 == pt2 :
    print(pt1)
else :
    print(pt1 if pt1 > pt2 else pt2)
    print(pt2 if pt1 > pt2 else pt1)
