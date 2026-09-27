name =' Vedant'
age = 20
print('My name is ',name,'i am ',age,' years old')
print('My name is %s i am %d years old'%(name,age))
print('My name is {1} and i am {0} years old '.format(name,age))
'f-string'
print(f'My name is {name} and i am {age} years old ')

n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
n3 = n1 + n2
n4 = n1 - n2
print(f'Addition of {n1} and {n2} is {n3}')
print(f'Subtraction of {n1} and {n2} is {n4}')