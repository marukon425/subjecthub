import math
import copy
# テスト結果の順位の順番に並べて表示する

class School:
    """ 国語の点数リスト """
    __jap_score_list = []

    """ 数学の点数リスト """
    __math_score_list = []
    
    """ 英語の点数リスト """
    __eng_score_list = []

    """ 学生リスト """
    student_list = []

    def get_student_list(self):
        return self.student_list
    
    """ 学生情報の追加 """
    def add_student(self, student) -> None:

        """ 常に平均点が高い順にソートして格納 """
        temp_list = []
        rank = 1
        is_add = False
        for stu in self.student_list:
            if is_add == False:
                if stu.get_score_average() < student.get_score_average():
                    # 追加
                    student.set_rank(rank)
                    rank += 1
                    temp_list.append(student)
                    self.add_score(student)
                    is_add = True

            stu.set_rank(rank)
            rank += 1
            temp_list.append(stu)
            self.add_score(stu)
            
        if is_add == False:
            student.set_rank(rank)
            temp_list.append(student)
            self.add_score(student)
        
        self.student_list = copy.deepcopy(temp_list)

    def add_score(self, student) -> None:
        """ 指定された学生の点数を追加する """
        self.__jap_score_list.append(student.get_jap_score())
        self.__math_score_list.append(student.get_math_score())
        self.__eng_score_list.append(student.get_eng_score())

    def get_jap_score_max(self) -> int:
        """ 国語の最高得点を取得 """
        return max(self.__jap_score_list)
    
    def get_math_score_max(self) -> int:
        """ 数学の最高得点を取得 """
        return max(self.__math_score_list)

    def get_eng_score_max(self) -> int:
        """ 英語の最高得点を取得 """
        return max(self.__eng_score_list)

    def get_jap_score_min(self) -> int:
        """ 国語の最低点を取得 """
        return min(self.__jap_score_list)
    
    def get_math_score_min(self) -> int:
        """ 数学の最低点を取得 """
        return min(self.__math_score_list)

    def get_eng_score_min(self) -> int:
        """ 英語の最低点を取得 """
        return min(self.__eng_score_list)

    def get_jap_score_ave(self) -> int:
        """ 国語の平均点を取得 """        
        ave = sum(self.__jap_score_list) / len(self.__jap_score_list)
        return math.floor(ave * 10 ** 2) / (10 ** 2)
    
    def get_math_score_ave(self) -> int:
        """ 数学の平均点を取得 """
        ave = sum(self.__math_score_list) / len(self.__math_score_list)
        return math.floor(ave * 10 ** 2) / (10 ** 2)

    def get_eng_score_ave(self) -> int:
        """ 英語の平均点を取得 """
        ave = sum(self.__eng_score_list) / len(self.__eng_score_list)
        return math.floor(ave * 10 ** 2) / (10 ** 2)

class Student:
    """ クラス内順位 """
    __rank = 0
    
    def __init__(self, name: str, no: str) -> None:
        """ コンストラクタ """
        self.name = name
        self.no = no
        self.ave_score = 0
        self.rank = 0
        self.test_result = TestResult("", 0, 0, 0)

    def set_test_result(self, result) -> None:
        self.test_result = result
        self.ave_score = self.test_result.get_score_average()

    def get_score_average(self) -> float:
        return self.ave_score

    def set_rank(self, rank) -> None:
        self.rank = rank
    
    def get_rank(self) -> int:
        return self.rank

    def get_jap_score(self) -> int:
        return self.test_result.jap_score
    
    def get_math_score(self) -> int:
        return self.test_result.math_score

    def get_eng_score(self) -> int:
        return self.test_result.eng_score
    
    def get_display_str(self):
        return "{} {:　<6}{:>4} {:>4} {:>4}  {:<6}".format(self.no, self.name, self.get_jap_score(), self.get_math_score(), self.get_eng_score(), self.ave_score)

class TestResult:
    """ テスト結果 """

    def __init__(self, no: str, jap_score: int, math_score: int, eng_score: int) -> None:
        """ コンストラクタ """
        self.no = no
        self.jap_score = jap_score
        self.math_score = math_score
        self.eng_score = eng_score

    """ 平均点取得 """
    def get_score_average(self) -> float:
        # 平均点を算出
        ave = (self.jap_score + self.math_score + self.eng_score) / 3
        # 小数点第３位を四捨五入して返却
        return round(ave, 2)

# 学校クラス作成
school = School()

# 学生オブジェクトの作成
sakuragi = Student("桜木花道", "001")
rukawa = Student("流川楓", "002")
mitsui = Student("三井寿", "003")
akagi = Student("赤木剛憲", "004")
miyagi = Student("宮城リョータ", "005")

# テスト結果オブジェクト作成
sakuragi_score = TestResult("001", 65, 45, 55)
rukawa_score = TestResult("002", 80, 88, 78)
mitsui_score = TestResult("003", 76, 73, 87)
akagi_score = TestResult("004", 96, 88, 99)
miyagi_score = TestResult("005", 70, 56, 75)

# 学生オブジェクトにテスト結果オブジェクトを設定して学校オブジェクトに追加
sakuragi.set_test_result(sakuragi_score)
school.add_student(sakuragi)
rukawa.set_test_result(rukawa_score)
school.add_student(rukawa)
mitsui.set_test_result(mitsui_score)
school.add_student(mitsui)
akagi.set_test_result(akagi_score)
school.add_student(akagi)
miyagi.set_test_result(miyagi_score)
school.add_student(miyagi)

# 学生毎のテスト結果の表示
print("No  名前　　　　 国語 数学 英語 平均点")
for student in school.get_student_list():
    print(student.get_display_str())

print()

# 科目毎の結果表示
print("国語の最高点：{}".format(school.get_jap_score_max()))
print("国語の最低点：{}".format(school.get_jap_score_min()))
print("国語の平均点：{}".format(school.get_jap_score_ave()))

print("数学の最高点：{}".format(school.get_math_score_max()))
print("数学の最低点：{}".format(school.get_math_score_min()))
print("数学の平均点：{}".format(school.get_math_score_ave()))

print("英語の最高点：{}".format(school.get_eng_score_max()))
print("英語の最低点：{}".format(school.get_eng_score_min()))
print("英語の平均点：{}".format(school.get_eng_score_ave()))
