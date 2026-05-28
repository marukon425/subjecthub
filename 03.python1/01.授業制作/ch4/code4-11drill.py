# データと型が一致かを判断
'''
isinstance(データ, 型)
データと型が一致：True
データと型が不一致：False
'''

num = 2
# num = "2"にすると文字になる⇒"int以外です"
if isinstance (2, int) :
    print("int型です")
else:
    print("int型以外です")