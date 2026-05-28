import random
def lucky_collar(fortune_num):
    fortune_num = random.randint(1, 14)
    if fortune_num == 1:
        fortune_num = '白'
    elif fortune_num == 3:
        fortune_num = '黒'
    elif fortune_num == 4:
        fortune_num = '赤'
    elif fortune_num == 5:
        fortune_num = '緑'
    elif fortune_num == 6:
        fortune_num = '黄'
    elif fortune_num == 7:
        fortune_num = '青'
    elif fortune_num == 8:
        fortune_num = '紫'
    elif fortune_num == 9:
        fortune_num = '橙'
    elif fortune_num == 10:
        fortune_num = '茶'
    elif fortune_num == 11:
        fortune_num = 'ピンク'
    elif fortune_num == 12:
        fortune_num = '灰'
    elif fortune_num == 13:
        fortune_num = 'オリーブ'
    elif fortune_num == 14:
        fortune_num = '黄緑'
    return fortune_num
color = lucky_collar(input('enterで入力'))
print(f'今日のラッキーカラーは{color}色です')

