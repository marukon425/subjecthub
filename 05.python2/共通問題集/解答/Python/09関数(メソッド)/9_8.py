def disp(array):
    """ 引数に指定された連想配列arrayの全要素を表示する """    

    # キー配列の取得
    keys = list(array.keys())

    # キー配列の要素数分ループ
    for key in keys:
        # キーに該当する値を取得
        value = array.get(key)

        # キーと値を表示
        print(key, "：", value, sep="")

# メイン処理

# 色情報を保持する連想配列の初期化
colors = {"赤":"red", "白":"white", "黒":"black", "青":"blue", "緑":"green"}

# 連想配列の全要素を表示する関数（メソッド）を呼び出す
disp(colors)
