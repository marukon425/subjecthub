# num_lst = []
# for i in range(0, 10):
#     num_lst = i**2
# print(num_lst)

# def di_num(num = 0):
#     print('hyouji', num)
# num = 9
# di_num()
# di_num(num)

def che_zer_han(sco):
    if 0 <= sco and sco <= 100:
        return True
    else:
        return False

def che_zer_ten(sco):
    if 0 <= sco and sco <= 10:
        return True
    else:
        return False

def fin_ill_sco(che_fun, sco_lst):
    count = 0
    flg = True
    for sco in sco_lst:
        count += 1
        if not che_fun(sco):
            print(count,'番目の点',sco,'は不正')
        if count == 0:
            print('点数なし')
        else:
            print('不正なし')

sco_lst1 = [2,8,5,1,6,9,8]
fin_ill_sco(che_zer_ten, sco_lst1)
sco_lst2 = [72, 89, 65, 101, 62, 94, 85]
fin_ill_sco(che_zer_han, sco_lst2)