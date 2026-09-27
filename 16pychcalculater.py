a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
print('Press: +,-,*,/')
ch=input('Enter your choice: ')
match ch:
    case '+':
        print('Addition: ',a+b)
    case'-':
        print('Subtraction: ',a-b)
    case '*':
        print('Multiplication: ',a*b)
    case '/':
        print('Division: ',a/b)
    case _:
        print('Invalid Input')