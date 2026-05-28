# 〇月〇日〇時〇分〇秒を表示
import datetime
print(datetime.datetime.now().strftime('%m月%d日%H時%M分%S秒'))


# １、２，３，　ダー　と１秒ごと
from time import sleep

target_time = 2

def down_timer(secs):
    count = 0
    for i in range(secs,-1, -1):
        count += 1
        print(count)
        sleep(1)
    print("ダー！！")

down_timer(target_time)
