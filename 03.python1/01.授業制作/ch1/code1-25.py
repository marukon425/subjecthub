# print関数の表示方法

# 名前は〇〇、年齢は〇歳、身長は〇cmです。

# 変数〇に名前、変数〇に年齢、変数〇に身長を設定
name = "丸山"

age = 19

height = 183

# アンパック代入：同時に代入
name2, age2, height = "尾田", 19, 160

# 【１】format関数の使用
# print("名前は{}、年齢は{}、身長は{}です" format(name, age, height ))

# 【２】f-stringの使用
print(f"名前は{name2}、年齢は{age}、身長は{height}です")


'''
趣味>>>〇〇
特技>>>△△△
朝食>>>□□□
fストリングで表示
趣味は〇〇、特技は△△△
'''

hobby = input("趣味を入力")
special_skill = input("特技を入力")
eaat = input("朝食を入力")

print(f"趣味は{hobby}、特技は{special_skill}、朝食は{eaat}を食べました。")