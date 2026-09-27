class Student:
    college_name='S.B.Jain'

    def setDetail(self,roll,name,marks):
        self.roll=roll
        self.name=name
        self.marks=marks

    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)

    @classmethod #---------class method - use for comman area of the
    def display_class(cls):
        print("College Name: ",cls.college_name)


    @staticmethod #-------- static method - use for creating square of the number
    def square(n):
        return n*n


s1=Student()
s1.setDetail(121,'Vedant',590)
s1.display()
Student.display_class()
print(Student.square(6))

s2=Student()
s2.setDetail(116,'Swan',552)
s2.display()
Student.display_class()
print(Student.square(8))

