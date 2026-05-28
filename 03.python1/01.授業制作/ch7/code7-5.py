# モジュールの取り込み

# mathモジュールから pi のみを取り込み(インポート)
from math import pi

# mathモジュールから floorメソッドを取り込み
from math import floor

# 円周率（3.141592）を表示
# mathモジュールのpi変数(円周率)を表示
print(f"円周率は{pi}です")

# 円周率を(小数点以下切り捨て)で表示
# mathモジュールのfloorメソッド math.floor()
print(f'小数点以下を切り捨てれば{floor(pi)}です')