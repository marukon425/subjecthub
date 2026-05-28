import sqlite3
'''
2文字の単語だけ格納完了
※ ただし「桃」の単語だけ漢字と読みが逆になってて修正必須
※ 3文字の単語はなぜか重複エラーで途中から格納できない不具合が発生、メインプログラムが完成し次第修正する

'''
# DBに単語を追加していく
# データベースにアクセス
con = sqlite3.connect('typing.db')

# sqliteを操作するカーソルオブジェクトを作成
cur = con.cursor()

# テーブルにデータを登録する
while True:
    try:
        data = input().split()
        if data[0] == 'break':
            break
        data1 = data[0]
        data2 = data[1]

        data_ = [(data1, data2, 13)]
        cur.executemany('INSERT INTO 単語 VALUES (?, ?, ?)',
                        data_)
    except:
        print(f'エラー単語：{data}')
        continue

# データベースをコミット
con.commit()
con.close