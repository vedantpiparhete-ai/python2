import csv
with open('Text File5.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name','Phone','City','Marks'])
    writer.writerow(['Vedant','8308227447','Nagpur','98'])
    writer.writerow(['Vangesh','0212021233','Nagpur','78'])
    writer.writerow(['Vansh','0212210132','Nagpur','45'])
    writer.writerow(['Krish','9889383922','Nagpur','26'])