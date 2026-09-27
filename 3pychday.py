days=int(input("Enter number of days: "))
year = days // 365
remainder = days % 365
month = remainder // 30
day = remainder % 30
print('Year: ',year)
print('Month: ',month)
print('Day: ',day)
print('Remainder: ',remainder)