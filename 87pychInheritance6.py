class p1:
    def set_a(self,a):
        self.a=a

    def welcome(self):
        print('WELCOME to Home')

class p2:
    def set_b(self,b):
        self.b=b

    def welcome(self):
        print('WELCOME to House')

class c(p1,p2):
    def set_c(self):
        self.c=self.a+self.b
        print('Addition: ',self.c)


c1=c()
c1.set_a(1)
c1.set_b(2)
c1.set_c()
c1.welcome()