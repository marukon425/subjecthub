import math

# 学生クラスの作成と情報の表示
class Student:
    """ 学生クラス """

    def __init__(self, name: str, no: str, jap_score: int, math_score: int, eng_score: int) -> None:
        """ コンストラクタ """
        self.name = name
        self.no = no
        self.jap_score = jap_score
        self.math_score = math_score
        self.eng_score = eng_score

    """ 平均点取得 """
    def get_score_average(self) -> float:
        # 平均点を算出
        ave = self.get_score_sum() / 3
        # 小数点第3位以下を切り捨てして返却        
        return math.floor(ave * 10 ** 2) / (10 ** 2)

    """ 合計点取得 """
    def get_score_sum(self) -> int:
        return self.jap_score + self.math_score + self.eng_score

# 学生オブジェクト作成
stu_a = Student("A", "001", 89, 65, 88)
stu_b = Student("B", "002", 80, 95, 64)
stu_c = Student("C", "003", 70, 80, 98)

# 学生情報の表示
print(stu_a.no, "番　", stu_a.name, "さん　", "平均点", stu_a.get_score_average(), sep="")
print(stu_b.no, "番　", stu_b.name, "さん　", "平均点", stu_b.get_score_average(), sep="")
print(stu_c.no, "番　", stu_c.name, "さん　", "平均点", stu_c.get_score_average(), sep="")
