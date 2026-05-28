# 入力されたファイル名に該当するファイルのデータを
# 指定されたファイル名でファイル作成し書き込む

from_file_name = input("コピー元ファイル名：")
to_file_name = input("コピー先ファイル名：")

# コピー元ファイルを読み込みモードで開く
from_file = open(from_file_name, "r")
# コピー先ファイルを書き込みモードで開く
to_file = open(to_file_name, "w")

# コピー元のデータをコピー先に書き込み
to_file.writelines(from_file.read())

# ファイルをクローズする
from_file.close()
to_file.close()
