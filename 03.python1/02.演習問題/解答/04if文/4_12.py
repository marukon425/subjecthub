# 満点合格・合格・不合格判定
pt = int(input("0～100までの得点（整数値）を入力してください: "))

if pt == 100 :
    print("満点合格です")
elif pt >= 60 :
    print("合格です")
else:
    print("不合格です")
