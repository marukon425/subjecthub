import csv
catalog = [('hat', 2000), ('shirt', 1000), ('scocks', 500)]
with open('catalog1.csv', 'w', encoding='utf-8', newline='') as file:
    csv.writer(file).writerows(catalog)