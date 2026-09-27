'''
Constructor: it is a special method which is mainly used to initialized object
it is defined as __init__()
As soon as object is created constructor gets called automatically and do not have to
call constructor specially(explicitly)
it can have only one constructor in a class because python does not support method
or constructor overload
'''

class Student():
    def __init__(self,name,age,rollno,percent):
        self.name=name
        self.age=age
        self.rollno=rollno
        self.percent=percent

    def display(self):
        print(f'Name: {self.name}\nAge: {self.age}\nRollno: {self.rollno}\nPercent: {self.percent}')


s1=Student('Vedant',20,121,99.99)
s1.display()

s2=Student('Gauri',13,108,96.98)
s2.display()