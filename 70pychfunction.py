def calculate(a,b):
    return a+b,a-b,a*b
add,sub,mul=calculate(40,20)
print("Addition: ",add)
print("Subtraction: ",sub)
print("Multiplication: ",mul)

print("\n--------------------------------------\n")

x=100  #global variable
def m1():
    # global x -- this is use for creating global into local
    x=10 #local variable
    print(x)
m1()
print(x)

print("\n--------------------------------------\n")

#lambda function
print("Lambda Function\n")

s=lambda n:n*n
print("Square: ",s(8))
c=lambda n:n*n*n
print("Cube: ",c(4))
add=lambda a,b: a+b
print("Add: ",add(30,34))

print("\n--------------------------------------\n")
