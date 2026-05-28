class info_main:
    name = ''
    old = 0
    birth = ''
    state = ''

    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

n = int(input('回数を入力>>>'))
student = [None]*n
for i in range(n):
    name, old, birth, state = input().split()
    student[i] = info_main(name, old, birth, state)

old_num = input()
for info_main in student:
    if info_main.old == old_num:
        print(info_main.name)
        break