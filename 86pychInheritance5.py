class shape:
    def set_radius(self,r):
        self.r=r

    def set_len_b(self,len,b):

        self.len=len
        self.b=b

    def set_side(self,side):
        self.side=side

class circle(shape):
    def cal_area(self):
        print(f'area of circle is {3.14*self.r**2}')


class rectangle(shape):
    def cal_area_rect(self):
        print(f'area of rectangle is : {self.len*self.b}')

    def cal_peri(self):
        print(f'perimeter of rectangle is : {2*(self.len*self.b)}')


class square(shape):
    def cal_area_sqr(self):
        print(f'area of square is : {self.side**2}')

c1=circle()
c1.set_radius(5)
c1.cal_area()

r1=rectangle()
r1.set_len_b(5,9)
r1.cal_area_rect()
r1.cal_peri()

s1=square()
s1.set_side(5)
s1.cal_area_sqr()
