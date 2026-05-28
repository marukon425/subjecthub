'''
【５】関数、例外処理
①関数：三角形の面積を計算し、小数点以下切り捨てで面積を戻す関数を作成する
②関数：底面積（①の結果）と高さを受け取り、小数点以下切り捨て三角柱の体積を戻す関数を作成すること
③メイン※数値以外が入力された場合は、例外処理を実行し再度入力させる
底辺を入力>>>5
高さを入力>>>8
底辺5、高さ8の三角形の面積は20です
三角柱の高さ>>>10
底面積20で高さ10の三角柱の体積は200です
 
底辺を入力>>>a
整数を入力してください
 
底辺を入力>>>5
高さを入力>>>8
底辺5、高さ8の三角形の面積は20です
三角柱の高さ>>>b
整数を入力してください
'''
# かんすう
# 関数１
def area(base, higt):
    return (base*higt)/2
# 関数２
def triangular_prism(result, higt_triangular):
    return result*higt_triangular



# メイン
while True:
    try:
        base = int(input('底辺を入力>>>'))
        higt = int(input('高さを入力>>>'))
        break
    except :
        print('整数を入力してください')

result = area(base, higt)

print(f'底辺{base}、高さ{higt}の三角形の面積は{result}です')
while True:
    try:
        higt2  = int(input('三角柱の高さ>>>'))
        break
    except:
        print('整数を入力してください')
result2 = triangular_prism(result, higt2)
print(f'底面積{result}で高さ{higt2}の三角柱の体積は{result2}です')

