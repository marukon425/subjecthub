# 四則演算を行う関数の定義
def add(x: int, y: int) -> int:
    """ 2つの引数の足し算をして結果を返す """
    return x + y

def sub(x: int, y: int) -> int:
    """ ２つの引数のひき算をして結果を返す """
    return x - y

def mul(x: int, y: int) -> int:
    """ ２つの引数のかけ算をして結果を返す """
    return x * y

def div(x: int, y: int) -> float:
    """ ２つの引数のわり算をして結果を返す """
    return int(x / y)

def mod(x: int, y: int) -> int:
    """ ２つの引数の剰余算をして結果を返す """
    return x % y

# 四則演算を行う高階関数の定義
def calc(x: int, y: int, f: 'function') -> 'Number':
    """ 引数として指定された関数による処理結果を返す """
    return f(x, y)


# ２つの整数値の入力
num1 = int(input("整数を入力してください："))
num2 = int(input("もう1つ整数を入力してください："))

print()
# 高階関数 calc に二つの整数値と、四則演算関数を
# 引数として渡して四則演算の結果を表示

# たし算：高階関数calcを使用してたし算を行い結果を表示
print('{} + {} = {}'.format(num1, num2, calc(num1, num2, add)))
# ひき算：高階関数calcを使用してひき算を行い結果を表示
print('{} - {} = {}'.format(num1, num2, calc(num1, num2, sub)))
# かけ算：高階関数calcを使用してかけ算を行い結果を表示
print('{} * {} = {}'.format(num1, num2, calc(num1, num2, mul)))
# わり算：高階関数calcを使用してわり算を行う
div = calc(num1, num2, div)
# 剰余：高階関数calcを使用して剰余算を行いわり算の結果と合わせて表示
rem = calc(num1, num2, mod)
print('{} / {} = {}'.format(num1, num2, str(div) + "…" + str(rem)))