def is_exists(num_array, target_num):
    """ 引数に指定された数値配列num_arrayの中に探索対象の数値target_numが存在するか判定し結果を返却する """
    # 返却値の初期化
    result = False

    # 配列の要素数分ループ
    for i in range(len(num_array)):
        num = num_array[i]

        # 探索対象の数値と同じ数値か判定
        if target_num == num: 
            # 数値が一致したので返却値をTrueに設定してループを終了
            result = True
            break
    
    return result

# メイン処理

# 配列の初期化
nums = [4,10,59,679,1991,3994,6789,19324]

# 探索対象の数値を入力させる
target = int(input("整数を入力してください："))

# 配列に探索対象が存在するか判定する関数（メソッド）を呼び出す
result = is_exists(nums, target)

# 探索結果によりメッセージを出し分ける
if result:
    print(target, "は配列に含まれています。", sep="")
else:
    print(target, "は配列に含まれていません。", sep="")
