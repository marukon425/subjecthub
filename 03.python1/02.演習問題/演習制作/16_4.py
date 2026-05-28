flag = True
while flag == True:
    a = input("入力")
    if a == "end":
        break
    else:
        with open('diary_dril.txt', 'a', encoding='utf-8') as file:
            file.write( a + '\n')