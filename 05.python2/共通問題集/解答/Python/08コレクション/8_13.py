# 学生番号と氏名の情報を保持し3件入力後表示

student_array = []

for _ in range(3):
    no = int(input("学生番号 = "))
    name = input("氏名 = ")
    # 学生番号と氏名をタプルで保持し配列に追加
    student_array.append((no, name))

print()
# 配列の全要素の表示
for info in student_array:
    print("学生番号：", info[0], " 氏名：", info[1], sep="")
