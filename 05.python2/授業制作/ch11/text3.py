with open('message.txt', encoding='utf-8') as file:
    # enumerate関数：インデックス(行番号)を取得する
    #                                ↓ ファイルを読み込んで行番号を1番から読み取る
    for count, text in enumerate(file, 1):
        print(count, text, end='')