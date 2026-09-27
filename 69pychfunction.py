#Position Argument
print("Position Argument")
def info(name, age):
    print('Name:',name)
    print('age:',age)
info('vedant',20)
info(13,'gauri')

print('\n----------------------------------------------\n')

#Keyword argument
print("Keyword argument")
def info(name,age):
    print('Name:',name)
    print('age:',age)
info(name='Vedant',age=20)
info(age=13,name='Gauri')

print('\n----------------------------------------------\n')

#default argument
print("default argument")
def info2(name,city='Nagpur'):
    print('Name:',name)
    print('City:',city)
info2('Vedant')
info2('Gauri','pune')

print('\n----------------------------------------------\n')

#Variable lenhgth arguent
def add(a,b):
    return a+b
print('Add:',add(10,20))

print('\n-------------\n')

def add2(a,b,c):
    return a+b+c
print('Add2:',add2(10,20,30))

print('\n-------------\n')

print("Variable lenhgth arguent")
def addition(*num):
    return sum(num)
print('Addition:',addition(10,20,30))
print('Addition:',addition(10,20,30,40))
print('Addition:',addition(10,20,30,40,50))

print('\n----------------------------------------------\n')

# **kwargs

print("**kwargs")
def defo(**data):
    print(data)
defo(name='Vedant',age=20,city='Nagpur')

