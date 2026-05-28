'''
ファイル名：diary_dril.txt

今日の一言>>>○○

【ファイルの中身】
今日の一言：○○
今日の一言：○○
'''

today = input('今日の一言＞＞＞')

with open('diary_dril.txt', 'a', encoding='utf-8') as file:
    file.write('今日の一言：' + today + '\n')