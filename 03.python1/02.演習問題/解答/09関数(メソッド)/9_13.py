import math

def get_odd_array(num_array):
    """ 引数に指定された配列から奇数の値を抽出して返却する """
    result_array = []

    for num in num_array:
        # 奇数の場合のみ返却する配列に追加
        if num % 2 != 0:
            result_array.append(num)

    return result_array

# メイン処理

array = [4, 9, 24, 45, 69, 22, 44, 51, 90, 78]

# 奇数のみ抽出して返却する関数（メソッド）の呼び出し
odd_array = get_odd_array(array)

# 結果を表示
for odd in odd_array:
    print(odd)
