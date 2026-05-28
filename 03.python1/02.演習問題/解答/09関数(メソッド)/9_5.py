def add(num1, num2):
    """ 引数に指定された２つの値を足し算して返却する """
    result = num1 + num2

    return result

def sub(num1, num2):
    """ 引数に指定された２つの値を引き算して返却する """
    result = num1 - num2
    
    return result

def mul(num1, num2):
    """ 引数に指定された２つの値を掛け算して返却する """
    result = num1 * num2
    
    return result

def div(num1, num2):
    """ 引数に指定された２つの値を割り算して返却する """
    if num2 == 0:
        # 割る数が0の場合は割り算を行わず0を返却する
        result = 0
    else:
        result = num1 / num2

    return result

def rem(num1, num2):
    """ 引数に指定された２つの値を剰余算して返却する """
    if num2 == 0:
        # 割る数が0の場合は剰余算を行わず割られる数を返却する
        result = num1
    else:
        result = num1 % num2

    return result

# メイン処理
input_num1 = int(input("1つ目の整数："))
input_num2 = int(input("2つ目の整数："))

# 足し算
add_result = add(input_num1, input_num2)
print(input_num1, "+", input_num2, "=", add_result, sep="")

# 引き算
sub_result = sub(input_num1, input_num2)
print(input_num1, "-", input_num2, "=", sub_result, sep="")

# 掛け算
mul_result = mul(input_num1, input_num2)
print(input_num1, "*", input_num2, "=", mul_result, sep="")

# 割り算
div_result = div(input_num1, input_num2)
print(input_num1, "/", input_num2, "=", div_result, sep="")

# 剰余算
rem_result = rem(input_num1, input_num2)
print(input_num1, "%", input_num2, "=", rem_result, sep="")
