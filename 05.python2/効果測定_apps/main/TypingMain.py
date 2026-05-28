from TypingNow import TypingNow
from datetime import datetime
from PaintText import PaintText 
from PaintBackground import PaintBackground
import datetime
import time
import os
txt_paint = PaintText()
txt_back = PaintBackground()

class TypingMain(TypingNow):
    def __init__(self):
        super().__init__()
        self.cm = TypingNow()

    def main_game(self, name):
        ans_count = 0
        bat_count = 0
        print('準備ができたら適当なキーを入力して開始します',end=time.sleep(3))
        input('>>>')
        for i in range(6):
            if i == 5:
                print('スタート!')
            else:
                print(5-i)
                time.sleep(1)
        # タイピングゲーム中
        # レベルのカウンタの初期化
        level_count = 0
        # 始めた時間を記録
        start_time = time.time()
        # 60秒に設定
        while True:
            # 解くごとにレベルが１上がる
            level_count += 1
            # レベルが14以上になったら14に固定する
            if level_count >= 13:
                level_count = 13
            read, japan = self.cm.question(level_count)
            # ↑ ひらがな表記
            # 正解するまで繰り返す　正常↓
            while True:
                flg = True
                if flg == False:
                    print(txt_back.red('違います'))
                print(japan)
                ans = input('>>>')
                if ans == 'stop':
                    return False
                elif ans == 'teat':
                    ans = read
                    continue
                if self.cm.check_answers(ans, read) == True:
                    ans_count += 1
                    print('正解')
                    flg = True
                    os.system('cls')
                    break
                else:
                    bat_count += 1
                    print('違います')
                    flg = False
                    os.system('cls')
            # タイマー
            if time.time() >= start_time + 60:
                print('終了!!')
                # 成績を表示
                time.sleep(2)
                print('正解した数：',end='')
                time.sleep(1)
                print(f'{ans_count}問')
                time.sleep(1)
                print('間違えた数:',end='')
                time.sleep(1)
                print(f'{bat_count}回')
                time.sleep(1)
                # 成績をデータベースに保存
                t = datetime.datetime.now().strftime('%Y年%m月%d日%H時%M分%S秒')
                self.cur.execute(f'INSERT INTO "{name}" VALUES (?, ?, ?)',(t, ans_count, bat_count))
                self.con.commit()
                return True
    # 成績を見るメソッド
    def see_result(self, user_name):
        self.cur.execute(f'SELECT * FROM "{user_name}"')
        rows = self.cur.fetchall()
        # データを出力（[]と()を外して変数に代入）
        print(f'{user_name}の記録')
        for row in rows:
            play_day, ans, bat_ans = row
            print(f'{play_day}  |  答えた数：{ans}  |  間違えた数：{bat_ans}')
