import csv
with open('Text File5.csv','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)