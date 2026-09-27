class Rectangle:
    #Area of Rectangle
    l=3
    b=2
    area=l*b

    def display(self):
        print('Length of Rectangle: ',self.l)
        print('Breadth of Rectangle: ',self.b)
        print('Area of Rectangle: ',self.area)

#Object Creation
s1=Rectangle()
s1.display()
s2=Rectangle()
s2.b=10
s2.l=20
s2.area=s2.l*s2.b
s2.display()