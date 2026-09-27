class G:
    def m1(self,a,b):
        self.a=a
        self.b=b

class P(G):
    def m2(self):
        self.c=self.a+self.b

class C(P):
    def m3(self):
        self.avg=self.c/3

    def display(self):
        print(f'First Number: {self.a}')
        print(f'Second Number: {self.b}')
        print(f'Sum of Third Number: {self.c}')
        print(f'Average of all 3 Number: {self.avg}')

c1=C()
c1.m1(10,20)
c1.m2()
c1.m3()
c1.display()