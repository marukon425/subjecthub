# 指定された数までの合計値算出
def get_total(target: int) -> int:
    if target < 1:
        return target
    return target + get_total(target-1)

# 入力
num = int(input("整数値を入力してください："))
# 合計値を算出
result = get_total(num)
# 結果を表示
print("1から{}の合計は{}です。".format(num, result))
