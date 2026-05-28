# 関数の定義
def get_multiple(target: int, num_list: list) -> list:
    """ 指定された倍数に該当する値を返却 """
    result_list = []

    for num in num_list:
        if num % target == 0:
            # targetの倍数なので結果リストに追加
            result_list.append(num)

    return result_list

# 高階関数の定義
def execute(num: int, num_list: list, f: "function") -> list:
    """ 引数として指定された関数による処理結果を返す """
    return f(num, num_list)

# メイン処理
num_list = [4,9,24,45,69,22,44,51,90,78]

# 高階関数executeを使用して3の倍数の配列を取得
result_list = execute(3, num_list, get_multiple)
# 結果を表示
for res in result_list:
    print(res)
