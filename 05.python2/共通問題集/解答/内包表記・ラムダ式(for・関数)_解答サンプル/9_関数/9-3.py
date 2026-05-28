"""指定された表示文字列を指定された回数分表示する.
    Parameters
    ----------
    str1 : str
        表示する文字列
    num1 : int
        表示回数

    Returns
    -------
        無し
"""
greeting = lambda str1,num1: [print(str1) for i in range(num1)]
# メイン処理
greeting("Hello", 3)
greeting("Good morning", 4)
greeting("Good evening", 2)