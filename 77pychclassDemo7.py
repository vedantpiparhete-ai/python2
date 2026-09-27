class employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

        self.da = 0.10* salary
        self.ta = 0.20* salary
        self.hra = 0.35* salary
        self.pf = 0.13* salary
        self.gross_salary = salary + self.da + self.ta + self.hra - self.pf


    def display(self):
        print("Employee Name:", self.name)
        print("Basic Salary:", self.salary)
        print("DA(10%):", self.da)
        print("TA(20%):", self.ta)
        print("HRA(35%):", self.hra)
        print("PF(13%):", self.pf)
        print("----------------------")
        print("Gross Salary:", self.gross_salary)

e1=employee('Vedant',1000000)
e1.display()