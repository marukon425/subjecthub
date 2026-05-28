import csv
with open('catalog1.csv', 'w', encoding='utf-8', newline='') as file:
    for row in csv.reader(file):
        print(row)