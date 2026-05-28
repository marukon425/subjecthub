'''
pc：お名前を教えてね
ユーザー：(自分の名前を入力)
PC：年齢も教えてね
ユーザー：(自分の年齢を入力)

PC：こんにちは〇〇さん
PC：〇歳ですね
pc:〇〇さんの年齢は〇さいですね
print(～　　int(age)+5　　～)

'''

# 【入力(input)させる】 pc：お名前を教えてね>>>
name = input("お名前を教えてね>>>")

# 【入力(input)させる】PC：年齢も教えてね>>>
age = input("年齢も教えてね")

print(name,age)

print("こんにちは", name, "さん")
print(age,"歳ですね")
print(name, "さんの年齢は", age, "ですね")
