
# for文の二重ループの内包表記
print([x*y for x in range(1, 10) for y in range(1, 10)])
# 内包表記じゃない版　↓
a = []
for x in range(1, 10):
    for y in range(1,10):
        a.append(x*y)
print(a)