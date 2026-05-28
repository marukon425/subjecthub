class OutOfIndex(BaseException):
    """ ユーザ定義例外「インデックス番号がリストの要素数より大きい値の時送出」 """
    pass

class MinusIndex(BaseException):
    """ ユーザ定義例外「インデックス番号が負の値の時送出」 """
    pass

def is_even(index, list):
    """ 引数として指定された数値リストから、引数として指定されたインデックス番号の要素が偶数であるか否かを調べる関数 """
    
    # インデックス番号が不正の場合
    if index >= len(list):        
        raise OutOfIndex

    # インデックス番号が負の場合
    if index < 0:
        raise MinusIndex

    result = False
    if list[index] % 2 == 0:
        # 値が偶数の場合返却値にTrueを設定
        result = True
    
    return result

# メイン処理

num_list = [1, 2, 3, 4, 5]
print("元のリスト = [{}]".format(num_list))

try:
    # インデックス番号を入力
    index = int(input("インデックス番号 = "))
    # 指定されたインデックスの値が偶数か判定する関数の呼び出し
    result = is_even(index, num_list)
    # 結果を表示
    if result == True:
        print("base_list[{}] = {} は偶数です。".format(index, num_list[index]))
    else:
        print("base_list[{}] = {} は偶数ではありません。".format(index, num_list[index]))

except OutOfIndex:
    print("領域外参照です。")

except MinusIndex:
    print("インデックス番号に負の値を指定しています。")
