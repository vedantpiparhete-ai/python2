from payroll61 import *
name=input('Enter your name: ')
basic=int(input('Enter your basic salary: '))
print('name: ', name)
print(f'Basic Salary: {basic}')
print(f'HRA: {calHra(basic)}')
print(f'DA: {calDa(basic)}')
print('----------------------------------')
print(f'Gross Salary: {calGross(basic)}')