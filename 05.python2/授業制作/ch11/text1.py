# massage.textファイルを開く
# モード：w ※書き込み ファイルがない場合は生成
# as 〇〇：〇〇が開いたファイルオブジェクト ⇒ file


with open ('message.txt', 'w', encoding='utf-8') as file:
    # 開いたオブジェクトのwriteメソッドを実行
    # \n : 改行コード
    file.write('Hello\n')
    file.write('Python\n')
    file.write('Programming\n')