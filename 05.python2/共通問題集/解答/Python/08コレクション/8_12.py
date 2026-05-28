# 5人分のテスト結果を入力して平均値を算出して表示する
import math

# 学生5人分の3科目の得点を格納するリスト
student_array = []

# 科目ごとの点数リスト
jap_array = []
math_array = []
eng_array = []
ave_array = []

for i in range(5):
    print(i+1, "人目の得点を入力", sep="")

    # 3科目の得点リスト
    subject_array = []

    for j in range(3):
        
        if j == 0:
            # 国語の点数を入力
            jap_score = int(input("国語の点数を入力："))
            subject_array.append(jap_score)
            jap_array.append(jap_score)
        elif j == 1:
            # 数学の点数を入力
            math_score = int(input("数学の点数を入力："))
            subject_array.append(math_score)
            math_array.append(math_score)
        elif j == 2:
            # 英語の点数を入力
            eng_score = int(input("英語の点数を入力："))
            subject_array.append(eng_score)
            eng_array.append(eng_score)
    
    # 3科目の平均点を格納
    ave = sum(subject_array) / len(subject_array)
    subject_array.append(math.floor(ave * 10 ** 2) / (10 ** 2))
    ave_array.append(math.floor(ave * 10 ** 2) / (10 ** 2))

    # 1人分の得点を格納
    student_array.append(subject_array)

# 科目ごとの平均点を格納
jap_ave = sum(jap_array) / len(jap_array)
math_ave = sum(math_array) / len(math_array)
eng_ave = sum(eng_array)  / len(eng_array)
total_ave = sum(ave_array)  / len(ave_array)

ave_array = [math.floor(jap_ave   * 10 ** 1) / (10 ** 1), 
             math.floor(math_ave  * 10 ** 1) / (10 ** 1),
             math.floor(eng_ave   * 10 ** 1) / (10 ** 1),
             math.floor(total_ave * 10 ** 1) / (10 ** 1)]
student_array.append(ave_array)

# 結果を表示
print()
print("      国語  数学  英語 平均点")
index = 0
for list in student_array:
    print("{:^4} {:>4}  {:>4}  {:>4}  {:<6}".format(index, list[0], list[1], list[2], list[3]))
    index += 1
