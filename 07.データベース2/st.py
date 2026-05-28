import datetime

n = int(input())
count = 0
sleep, wake = input().split(" ")

sleep = list(map(int, sleep.split(":")))
wake = list(map(int, wake.split(":")))

sleep = datetime.datetime(2023, 4, 1, sleep[0], sleep[1])
wake = datetime.datetime(2023, 4, 1, wake[0], wake[1])

for i in range(n-3):
    s, w = input().split(" ")
    s = list(map(int, s.split(":")))
    w = list(map(int, w.split(":")))

    s = datetime.datetime(2023, 4, 1, s[0], s[1])
    w = datetime.datetime(2023, 4, 1, w[0], w[1])
    if (sleep - s).days <= 30 and (wake - w).days:
        count += 1
    sleep, wake = input().split(" ")

    sleep = list(map(int, sleep.split(":")))
    wake = list(map(int, wake.split(":")))

    sleep = datetime.datetime(2023, 4, 1, sleep[0], sleep[1])
    wake = datetime.datetime(2023, 4, 1, wake[0], wake[1])

print(count)
