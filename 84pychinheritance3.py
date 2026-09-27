class p:
    def a1(self,b,l):
        self.b=b
        self.l=l

class c(p):
    def m2(self):
        self.a2=self.l*self.b
        print(f'Area of Re-Triangle: {self.a2}')

    def m3(self):
        self.a3=2*(self.l+self.b)
        print(f'Perimeter of Re-Triangle: {self.a3}')

m1=c()
m1.a1(6,7)
m1.m2()
m1.m3()