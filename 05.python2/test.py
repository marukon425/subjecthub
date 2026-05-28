count = 0
nums = [111, 222, 333, 444, 555, 666, 777, 888, 999, 000]
p = []
for i in range(333333):
    count += 1
    #100の位まで飛ばす
    if count >= 100:
        for j in nums:
            if str(j) in str(count):
                p.append(count)
                print(count)


print(sum(p))


