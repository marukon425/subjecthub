# for文(繰り返す)の 学習

'''for文の使い方
for 変数 in 回数 ※range(回数)
    繰り返す処理

※ inの後ろから「リスト」から「変数」に
   一つずつ代入し、処理を繰り返す
'''

'''pythonは楽しいを三回繰り返す
〇回目:pythonは楽しい
〇回目:pythonは楽しい
〇回目:pythonは楽しい
'''

# range(〇):0～〇未満
for count in range (3):
    print (f"{count + 1}回目：pythonは楽しい")# ←０から始まらない

# range(〇, △):〇～△未満
# 5-10まで表示
for count in range (5, 11):
    print (f"{count}回目：pythonは楽しい")

