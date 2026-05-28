# 1から10までの奇数のみ表示
[print(i, end=" ") for i in range(1,11,2)]

# 別解
# [print(i, end=" ") for i in range(1,11) if i % 2 != 0]

# ジェネレータ式
ge = (i for i in range(1,11) if i % 2 != 0)
for i in ge:
    print(i)