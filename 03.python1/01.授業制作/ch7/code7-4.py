# モジュールの取り込み

# mathモジュールを取り込み(インポート)
# mathモジュール：数学計算に関する処理（機能など）
# as をつけて、別名で管理
import math as m # mathをmとして使用

# 円周率（3.141592）を表示
# mathモジュールのpi変数(円周率)を表示
print(f"円周率は{m.pi}です")

# 円周率を(小数点以下切り捨て)で表示
# mathモジュールのfloorメソッド math.floor()
print(f'小数点以下を切り捨てれば{m.floor(m.pi)}です')