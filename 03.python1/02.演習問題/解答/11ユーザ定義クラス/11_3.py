# 計算実行と結果の表示

class CalcExecutor:
    """ 計算実行クラス """
    x = 0
    y = 0

    def __init__(self, x: int, y: int) -> None:
        CalcExecutor.x = x
        CalcExecutor.y = y

    """ 合計値を取得 """
    def sum(self) -> int:
        res = 0
        for num in range(CalcExecutor.x, CalcExecutor.y + 1):
            res += num
        
        return res

class Main:

    """ メインクラス """
    def execute(self) -> None:
        # 計算実行インスタンスの生成
        calc_exec = CalcExecutor(100, 200)
        # 合計値を取得
        total = calc_exec.sum()
        # 結果を表示
        print("{}から{}の合計値は{}です。".format(calc_exec.x, calc_exec.y, total))

# メインクラスの生成とメイン処理実行
main = Main()
main.execute()