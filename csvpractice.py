import csv

f = open('vs_chart.csv', 'r')
reader = csv.reader(f)

for line in reader:
    print(line[0])