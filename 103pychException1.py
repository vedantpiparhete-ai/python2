print("Hello i am Vedant")
f1=int(input("Enter first number: "))
f2=int(input("Enter second number: "))
try:
    division=f1/f2
    print('division is:',division)
except ZeroDivisionError:
    print("Cannot divide by zero")
print("okay Bye see you tommorow")