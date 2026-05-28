

def deep_copy(lst):
    new_list = []
    for val in lst:
        new_list.append(val)
    return new_list


# メイン
score = [10,20,30]
i1 = id(score)
score = deep_copy(score)
i2 = id(deep_copy(score))
print('元のリスト:{}',(i1))
print('上書きid:',deep_copy(i2))
if i1 != i2:
    print('成功')
    print(id(i1))