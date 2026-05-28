# 「領域外参照」例外を補足

base_list = [1, 2, 3, 4, 5]
print("base_list =", base_list)

try:
    index = int(input("インデックス番号 = "))

    # 入力されたインデックスにある値を取得して表示
    value = base_list[index]
    print("base_list[{}] = {}".format(index, value))

except IndexError:
    print("領域外参照です")

finally:
    print("終了")
