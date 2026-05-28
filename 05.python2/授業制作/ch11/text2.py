# モード：'r' ※読み込みファイルがない場合はエラー
with open('message.txt', 'r', encoding='utf-8') as file:
    print(file.read())