class p:
    def m1(self,r):
        self.r=r

class c(p):
    def m2(self):
        self.area=3.14*self.r**2
        print(f'Area of circle: {self.area}')

    def m3(self):
        self.circum=2*3.14*self.r
        print(f'Circumference of circle: {self.circum}')

c1=c()
c1.m1(5)
c1.m2()
c1.m3()

