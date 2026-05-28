# 素数判定
num = int(input("数値入力："))
# 素数フラグ
is_prime = True

for i in range(2, num):
    if num % i == 0:
        print(str(num), "は素数ではありません。", )
        # 素数フラグをFalseにしてループ処理終了
        is_prime = False
        break

# 素数フラグがTrueの時のみ以下を表示
if is_prime:
    print(str(num), "は素数です。")
