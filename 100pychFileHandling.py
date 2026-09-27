import csv
with open('Text File6.txt','r') as f:
    reader=csv.reader(f)
    for row in reader:
        print(row)