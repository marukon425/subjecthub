import requests
# 変数rにhtmlファイルを取得
# requestsモジュールのgetメソッドを実行
r = requests.get('http://higpen.jellybean.jp/')
# rオブジェクトの 変数textを表示
print(r.text)

# 〇〇.▢▢ ← 変数、入れ物
# 〇〇.▢▢()  メソッド、処理
