


a_len = input()
a_ls = input().split()
b_len = input()
b_ls = input().split()

for i in range(len(a_ls)):
    ln = 0
    for j in range(len(b_ls)):
        if a_ls[i] == b_ls[j]:
            ln += 1
    print(f"{a_ls[i]}:{ln}")
