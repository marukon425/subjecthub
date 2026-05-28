def disp_info(school, name):
    """引数に指定された学校名と名前を表示する.

    Parameters
    ----------
    school : str
        学校名
    name : str
        名前

    Returns
    -------
        無し
    
    """
    print("学校名：", school, sep="")
    print("名前：", name, sep="")

# メイン処理
disp_school_name = "東京情報クリエイター工学院専門学校"
disp_your_name = "竹井一馬"

# 情報表示関数（メソッド）の呼び出し
disp_info(disp_school_name, disp_your_name)