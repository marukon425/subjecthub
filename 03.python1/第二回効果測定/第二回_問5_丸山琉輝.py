# 小数点を切り捨てるためにmathモジュールを使用
import math


#### 関数
# 面積を求める関数
def circle_area(radius):
    # 底面積を計算し、計算結果をメインに返す
        return math.floor(radius * radius* 3.14)

# 体積を求める関数
def cylinder_volume(area, hight):
    # 円柱の体積を計算し、計算結果をメインに戻す
    return math.floor(area * hight)


#### メイン
# 例外処理
try:
    # 半径を入力
    radius = int(input('半径を入力：'))
except ValueError:
    # 整数以外が入力された場合'整数を入力してください'と表示
    print('整数を入力してください')
# 計算結果を表示
print(f'半径が{radius}の面積は{circle_area(radius)}です')    

# 例外処理
try:
    # 円柱の高さを入力
    hight = int(input('高さを入力：'))
except ValueError:
    # 整数以外が入力された場合'整数を入力してください'と表示
    print('整数を入力してください')

# 底面積の計算結果を変数(area)に代入しておく
area = circle_area(radius) 
# 計算結果を表示
print(f'底面積が{area}で高さが{hight}の円柱の体積は{cylinder_volume(area, hight)}です')
