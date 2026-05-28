# 外部ライブラリ(PIL)からImageを取り込む
from PIL import Image

# Imageのnewメソッドを実行
#引数：        色指定↓　  サイズ↓　　　   各色↓ 
image = Image.new('RGB', (640, 480), (255, 255, 0))

# yellow.pngというファイル名で保存する(saveメソッドで保存する)
image.save('yellow.png')  

# ターミナルで cd をしてファイルを移動する(lsでファイルを参照してもできる