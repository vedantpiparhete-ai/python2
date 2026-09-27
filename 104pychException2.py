a=int(input("Enter first number: "))
try:
    c=a/'a'
    print('division: ',c)
except ZeroDivisionError:
    print('cannot divide by zero')
except ValueError:
    print('only numeric values are accepted')
except TypeError:
    print("only numbers")
print("Normal termination")