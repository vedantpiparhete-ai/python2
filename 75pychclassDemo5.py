class student():
    def setdetail(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3
        #self.total=m1+m2+m3
        #self.perc=m1+m2+m3/300*100

    def display(self):
        print(f'Name of Student: {self.name} ')
        print(f'Subject1 Marks: {self.m1}')
        print(f'Subject2 Marks: {self.m2}')
        print(f'Subject3 Marks: {self.m3}')
        print(f'Total Marks Obtain: {self.total()}')
        print(f'Percentage Score: {self.per()}')
        print(f'Result: {self.result()}')
        print('\n--------------------------------------------------------------\n')

    def total(self):
        self.total=self.m1+self.m2+self.m3
        return self.total

    def per(self):
        self.per=self.total/300*100
        return self.per

    def result(self):
        if self.per>=35:
            return "Pass"
        else:
            return "Fail"

m1=student()
m1.setdetail('Vedant',98,96,98,)
m1.display()

m2=student()
m2.setdetail('Gauri',98,95,96)
m2.display()

m3=student()
m3.setdetail('Swaan',98,95,96)
m3.display()