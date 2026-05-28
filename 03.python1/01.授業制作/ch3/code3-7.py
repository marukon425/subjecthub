'''
国語の得点(jp)
数学の得点(ma)

両科目とも80点以上  ⇒  合格
'''

jp = int(input("国語の点数を入力してください"))
ma = int(input("数学の点数を入力してください"))

if jp >= 80 and ma >=80:
    print("合格")
else:
    print("不合格")