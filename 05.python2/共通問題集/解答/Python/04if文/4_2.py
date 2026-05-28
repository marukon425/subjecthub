# 国語と英語の点数の満点判定
print("0～100までの得点（整数値）を2つ入力してください")
japanese = int(input("国語の得点："))
english = int(input("英語の得点："))

# 国語も英語も100だった場合「満点です」と表示する
if japanese == 100 and english == 100 :
    print("満点です")
