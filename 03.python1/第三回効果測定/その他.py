'''
class info:
    def __init__(self, name, old, birth, state):
        self.name =  name
        self.old = old
        self.birth = birth
        self.state = state
n = int(input())

stu = [None]*n
for i in range(n):
    name, old, birth, state = input().split()
    stu[i] = info(name, old, birth, state)

# バブルソート
for i in range(n):
    for j in range(i + 1, n):
        if stu[i].old > stu[j].old:
            stu[i], stu[j] = stu[j], stu[i]


for info in stu:
    print(info.name, info.old, info.birth, info.state)
'''
# class info:
#     def __init__(self, name, old, birth, state):
#         self.name =  name
#         self.old = old
#         self.birth = birth
#         self.state = state

#     def change_name(self, name):
#         self.name = name

# n, p = map(int, input('>').split())
# stu = [None]* n

# for i in range(n):
#     name, old, birth, state = input('>').split()
#     stu[i] = info(name, old, birth, state)
# for info in stu:
#     print(f'befor:{info.name, info.old, info.birth, info.state}')

# for i in range(p):
#     c, name_ = input('>').split()
#     stu[int(c) - 1].change_name(name)

# for info in stu:
#     print(info.name, info.old, info.birth, info.state)

# class Student:
#     def __init__(self, name, old, birth, state):
#         self.name = name
#         self.old = old
#         self.birth = birth
#         self.state = state

#     def change_name(self, name):
#         self.name = name


# n, k = [int(x) for x in input().split()]

# roster = [None] * n
# for i in range(n):
#     name, old, birth, state = input().split()
#     roster[i] = Student(name, old, birth, state)

# for i in range(k):
#     index, new_name = input().split()
#     roster[int(index) - 1].change_name(new_name)

# for student in roster:
#     print(student.name, student.old, student.birth, student.state)

# n = int(input())
# for i in range(1, n+1):
#     for j in range(1, n+1):
#         if j == n:
#             print(i * j)
#         else:
#             print(i * j, end=' ')


# n, m = input().split()
# n = int(n)
# m = int(m)
# for i in range(n):
#     if i+1 == n:
#         print(f'{i+1}')
#     else:
#         print(i+1, end=' ')
# for j in range(m):
#     if j+1 == m:
#         print(f'{j+1}')
#     else:
#         print(j+1, end=' ')


# n = int(input())
# m_lst = list(map(int,input().split()))
# for i in range(n):
#     for j in range(m_lst[i]):
#         if j + 1 == m_lst[i]:
#             print(j + 1)
#         else:
#             print(j + 1, end=' ')
'''
n, m = map(int, input('>').split())
a_lst = list(map(int, input('>').split()))
b_lst = list(map(int, input('>').split()))

for i in range(m):
    for j in range(b_lst[i]):
        if j + 1 == b_lst[i]:
            print(a_lst[j])
            a_lst.remove(a_lst[i])
        else:
            print(a_lst[j], end=' ')
            a_lst.remove(a_lst[i])
'''
judgment = 'No'
n, m = map(int, input().split())
s = []
for i in range(n):
    s.append(int(input())) 
r = m in s
if r == True:
    print('Yes')
else:
    print('No')