############# 関数 #############
#関数名；add_sufix()
# 処理：受け取ったリストオブジェクトに'さん'をつけて返す
# 引数：names ※リストオブジェクトの保存先(管理番号)
# 戻り値：names ※リストオブジェクトの保存先(管理番号)
def add_sufix(names):
    # namesリストオブジェクトに'さん'を追加する
    for i in range(len(names)):# range(リストの要素数)
        names[i] = names[i] + "さん"
    return names

############# メインプログラム #############
# リストオブジェクトの作成
before_names = list(('松田', '浅木', '工藤'))
# before_nameを引数として、add_sufixを呼び出し、戻り値をafter_namesに格納
# 引数：before_namesの保存先（管理番号）
# 戻り値：befor_namesの保存先(管理番号)
after_names = add_sufix(before_names)
# befor_namesとafter_namesを表示
print(f'before_names:{before_names}')
print(f'after_names:{after_names}')





