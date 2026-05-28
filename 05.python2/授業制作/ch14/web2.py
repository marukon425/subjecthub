# web情報を取得するモジュールをインポート
from urllib.request import urlopen

# webページを取得し、オブジェクト名をfileに変更
with urlopen('http://higpen.jellybean.jp') as file:
    # lineにfileのHTMLを一行一行渡す
    for line in file:
        # htmlを出力 ※文字コードの指定が必要
        print(str(line, encoding='utf-8'), end='')#ユニコードに変更