# 関数の復習
# メインで２数値を入力
# 関数へ２つの数値を送り、足し算をして結果を返す
# メインで結果を表示

# ======関数=====
def add(num1,num2):
    return num1 + num2

# =====メイン=====
num1 = int(input('１つめの数字>>>'))
num2 = int(input('２つめの数字>>>'))
print((add(num1, num2)))