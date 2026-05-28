'''
【１】ファイルの書き込み
　①5回文字を入力し、リストへデータを追加
　②リストに保存されているデータを一つずつファイルに書き出し
　１つ目の文字列>>>〇〇〇
　２つ目の文字列>>>△△△
　３つ目の文字列>>>□□□
　４つ目の文字列>>>◇◇◇
　５つ目の文字列>>>☆☆☆

　※この時点でリストは['〇〇〇', '△△△', '□□□', '□□□', '☆☆☆']
　※ファイル（taisaku01.txt）へ書き込み処理
　※ファイルの内容
　　〇〇〇
　　△△△
　　□□□
　　◇◇◇
　　☆☆☆


'''

# for i in range(5):
#     text = input(f'{i+1}つ目の文字列>>>')
#     file = open('diary.tet', 'a', encoding='utf-8') as file:
#     file.write(text +'\n')
#     with open('diary.tet', 'a', encoding='utf-8') as file:
#     # データを書き込み
#     file.write(text + '\n')

with open('diary.tet', 'a', encoding='utf-8') as file:
    for i in range(5):
        text = input(f'{i+1}つ目の文字列>>>')
        file.write(text + '\n')