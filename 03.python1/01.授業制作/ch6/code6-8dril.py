############# 関数 #############
#関数名；add()
# 処理：受け取った変数に１を加算て返す
# 引数：nam
# 戻り値：nam
def add(num):
    num += 1
    return num

###############################################

#関数名；add_list
# 処理：受け取った変数に１を加算て返す
# 引数：nam:num_list※リストオブジェクトの保存先(管理番号)
# 戻り値：nam_list※リストオブジェクトの保存先(管理番号)
def add_list(num_list):
    for i in range(len(num_list)):
        num_list[i] = num_list[i] + 1
    return num_list
#################################################

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

############# メインプログラム #############
### 通常の変数(add)の場合
# before_num に 10 を設定
before_num  = 10
# before_num を 引数として add関数を呼び出し、after_numに格納
after_num = add(before_num)
# before_num と affter_num を表示
print(f'before_numは{before_num}')# 変数は(10)を送る
print(f'after_numは{after_num}')

### リストオブジェクト(add_list)の場合
# before_num_listオブジェクト に 10,20,30 を設定
before_num_list = [10, 20 ,30]
# before_num_listを複製し、別のリストを送る
# 複製用の空リストを作成 【防御的コピー】
before_num_list2 =[]
# before_num_listからbefore_num_list2に１つずつ追加
for i in before_num_list:
    before_num_list2.append(i)
    # 複製したリストを関数へ送る

# before_num_list を 引数として add_list関数を呼び出し、after_num_listに格納
after_num_list = add_list(before_num_list)# オブジェクトは保存先(アドレス)を送る
# before_num_list と affter_num_list を表示
print(f'before_num_list2は{before_num_list2}')
print(f'after_num_listは{after_num_list}')

