
# 引数として指定された範囲の偶数値の合計を
# 再帰を使用して計算してその合計値を返す
def get_even_total(start: int, end: int) -> int:
  if end <= start:  # 終了条件
    # startがend以上で偶数ならstartを返す、奇数なら0を返す
    return 0 if start % 2 != 0 else start

  elif end % 2 == 0:  # 偶数の時
    # 今までの合計値に加算し、再帰呼び出しする
    return end + get_even_total(start, end - 1)

  else: # 偶数でないとき
    # 合計値に加算せず、再帰呼び出しする
    return get_even_total(start, end - 1)

# メイン処理

start = int(input("開始数を整数値で入力してください："))
end = int(input("終了数を整数値で入力してください："))

# 指定された開始数から終了数までの偶数値の合計をもとめて表示
total = get_even_total(start, end)
print("{} から {} までの偶数値の合計 = {}".format(start, end, total))