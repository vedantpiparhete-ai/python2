class Employee:
    def __init__(self,name,basicsalary):
        self.name=name
        self.basicsalary=basicsalary
    def calda(self):
        return self.basicsalary*10/100
    def calta(self):
        return self.basicsalary*20/100
    def calhra(self):
        return self.basicsalary*35/100
    def calpf(self):
        return self.basicsalary*13/100
    def calgross(self):
        return self.basicsalary+self.calda()+self.calta()+self.calhra()-self.calpf()
    def display(self):
        print(f'Name:',self.name)
        print(f'Basic Salary:',self.basicsalary)
        print(f'DA:',self.calda())
        print(f'TA:',self.calta())
        print(f'HRA:',self.calhra())
        print(f'PF:',self.calpf())
        print(f'Gross Salary:',self.calgross())
        print(f'------------------------------------------')
s1=Employee('Manan',50000)
s1.display()
s2=Employee('Kunal',80000)
s2.display()
s3=Employee('Rushi',60000)
s3.display()