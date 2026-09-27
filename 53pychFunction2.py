def add(a,b):
    c=a+b
    print("Addition: ",c)

def sub(a,b):
    c=a-b
    print("Subtraction: ",c)

def mult(a,b):
    c=a*b
    print("Multiplication: ",c)

def div(a,b):
    c=a/b
    print("Division: ",c)

def module(a,b):
    c=a%b
    print("Module: ",c)

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))

add(a,b)
sub(a,b)
mult(a,b)
div(a,b)
module(a,b)