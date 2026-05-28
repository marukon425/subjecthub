from TypingRog import TypingRog
class TypingNow(TypingRog):
    # 出題する問題を出すメソッド
    def question(self, level):
        # ランダムに単語を抽出
        question = self.cur.execute('SELECT word, japanese FROM 単語 WHERE word_level = ? ORDER BY RANDOM() LIMIT 1 ',(level,)).fetchone()
        # タプルになってる問題を返す
        return question
        
    # 出された問題に対して答えが合ってるか管理するメソッド
    def check_answers(self, answer, example_answer):
        if answer == example_answer:
            return True
        else:
            return False
