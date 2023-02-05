import csv

with open('data2.csv', 'r') as fr:
    reader = csv.reader(fr)
    for row in reader:
        print(row)
