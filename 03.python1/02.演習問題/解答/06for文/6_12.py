# 三角形を描画
for i in range(1, 11):
    # ＊文字列
    ast_str = ""
    # スペース文字列
    sp_str = ""
    # スペースの数
    sp_num = 10 - i

    # ＊文字列の作成
    for _ in range(0, i):
        ast_str += "＊"

    # スペース文字列の作成
    for _ in range(0, sp_num):
        sp_str += " "

    # 1行分表示
    print(sp_str, ast_str, sp_str, sep="")
