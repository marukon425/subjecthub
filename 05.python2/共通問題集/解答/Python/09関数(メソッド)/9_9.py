import math

def get_circle_length(radius):
    """ 引数に指定された半径を元に円周を算出し返却する """
    length = (radius + radius) * math.pi
    return length

def get_circle_are(radius):
    """ 引数に指定された半径を元に円の面積を算出し返却する """
    area = radius * radius * math.pi
    return area

# メイン処理
radius = float(input("半径を入力してください："))

# 円周
length = get_circle_length(radius)
print("半径", radius, "の円周は", "{:.3f}".format(length), sep="")

# 円の面積
area = get_circle_are(radius)
print("半径", radius, "の円の面積は", "{:.3f}".format(area), sep="")
