# ================ディクショナリの学習================
'''
リスト：自動的に添え字がつく(0.1,2,3,..)
　　　　⇒[要素0,要素1,要素2,....]
ディクショナリ：自分で添え字のようなキーをつける
　　　　　　　　⇒{キー１：要素1,　キー2：要素2}

'''
# ディクショナリ関数score
# キーnet に 60、 キーdb に 80、 キーsc に 50
# {}になったらディクショナリ ''なのは「文字」だから
score = {'net':60, 'db':80, 'sc':50}
# scoreを表示
print(score)
# scoreのnet番目を表示
print(score['net'])

# 変更前のscoreを表示　変更前：〇〇
print(f"変更前{score}")
# score の db を 90 に変更
score['db'] = 90
# score に pro 65 を追加
score['pro'] = 65
# 変更後のscoreを表示　変更後：〇〇
print(f"変更後{score}")

# scoreの sc を削除
del score['sc']
print(f'削除後：{score}')

serch = input('検索')
print(score[serch])


'''
listとdictionaryじゃ変更・削除の使い方が違う！！！
'''