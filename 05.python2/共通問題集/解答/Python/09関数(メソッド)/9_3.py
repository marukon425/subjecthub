def disp_infos(disp_str, num):
    """指定された表示文字列を指定された回数分表示する.

    Parameters
    ----------
    disp_str : str
        表示する文字列
    num : int
        表示回数

    Returns
    -------
        無し
    
    """
    for _ in range(num):
        print(disp_str)

# メイン処理
disp_infos("Hello", 3)
disp_infos("Good morning", 4)
disp_infos("Good evening", 2)
