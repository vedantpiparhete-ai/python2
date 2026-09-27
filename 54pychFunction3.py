#Rectangle
def perimeter(l,w):
    c=2*l+w
    print("Perimeter of a rectangle: ",c)

def area(l,b):
    area=l*b
    print("Area of a rectangle: ",area)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

area(a,b)
perimeter(a,b)
