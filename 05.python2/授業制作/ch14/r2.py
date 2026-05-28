import requests
# 変数rにhtmlファイルを取得
# requestsモジュールのgetメソッドを実行
r = requests.get('http://higpen.jellybean.jp/')

# ファイル名download2.htmlを開き(作り)
#                             ↓ バイナリデータを書き込み
with open('download2.html', 'wb') as file:
    # 変数rのHTMLを入れる
    file.write(r.content)