import time

print("5秒間でできるだけ多くの文字を入力してください！")
time.sleep(1)
print("よーい、スタート！")

start = time.time()
user_input = ""

while time.time() - start <= 5:
    user_input += input()

print("\n終了！")
print(f"入力された文字数: {len(user_input)}")
print(f"内容: {user_input}")