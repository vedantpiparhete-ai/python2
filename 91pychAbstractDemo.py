from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass

class circle(shape):
    def set_radius(self,r):
        self.r=r

    def area(self):
        print('Area of circle: ',3.14*self.r**2)


class Rectangle(shape):
    def set_length(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        print('Area of rectangle: ',self.l*self.b)

c1=circle()
c1.set_radius(2)
c1.area()

r1=Rectangle()
r1.set_length(4,6)
r1.area()