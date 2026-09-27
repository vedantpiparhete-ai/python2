sub1 =int(input("Enter marks of subject 1: "))
if sub1 >= 40:
    sub2 = int(input('Enter marks of subject 2: '))
    if sub2 >= 40:
        print('ALL CLEAR you are Pass')
    else:
        print('Fail')
        print('Try Again Next Time')
else:
    print('Fail ')