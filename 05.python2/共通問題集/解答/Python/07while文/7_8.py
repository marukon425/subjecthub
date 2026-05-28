# フィボナッチ数列を表示
num1 = 0
num2 = 1
loop = 1
disp_str = ""

# 1000以下の項を表示
while True:
    if loop == 1:
        disp_str += str(num1)
    elif loop == 2:
        disp_str += str(",")
        disp_str += str(num2)
    else:
        num1, num2 = num2, num1 + num2
        if num2 > 1000:
            break

        disp_str += str(",")
        disp_str += str(num2)
    
    loop += 1

print(disp_str)
