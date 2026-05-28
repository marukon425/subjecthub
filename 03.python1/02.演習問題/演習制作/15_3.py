while True:
    try:
        base_list = [1, 2, 3, 4, 5]
        index = int(input('インデックス番号 ='))
        print(base_list[index])
        break
    except:
        print('領域外参照です')
