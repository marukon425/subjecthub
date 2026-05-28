# 1から10までの値を表示
[print(i, end=" ") for i in range(1,11)]

# ジェネレータ式
ge = (i for i in range(1,11))
for i in ge:
    print(i)