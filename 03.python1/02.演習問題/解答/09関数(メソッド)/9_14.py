# 足し算結果または平均値を返却する関数

def calc(num1, num2, *nums):
    """ 引数が2つの場合は足し算結果、3つの場合は平均値を返却 """
    result = 0

    # 可変引数の要素数で判定
    if len(nums) == 0:
        # 引数が2つなので足し算する
        result = num1 + num2
    else:
        # 引数が3つなので平均値を求める
        result = (num1 + num2 + nums[0]) / 3

    return result

# メイン処理

# 足し算の結果をする関数（メソッド）の呼び出し
add_result = calc(734, 78)
# 平均値を返却する関数（メソッド）の呼び出し
ave_result = calc(794, 710, 645)

# 結果表示
print("734 + 78 =", add_result)
print("(794 + 710 + 645) / 3 =", ave_result)
