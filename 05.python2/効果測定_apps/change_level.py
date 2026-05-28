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

cur.execute('UPDATE 単語 SET japanese = ? WHERE japanese = ?', (' 無知は時として罪になる',  '無知は時として罪になるbreak'))

# データベースをコミット
con.commit()
con.close