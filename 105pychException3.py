a=int(input("Enter first number: "))
try:
    c=a/'a'
    print("division: ",c)
except(ZeroDivisionError,ValueError,TypeError) as e:
    print(f"Exception raised: {e}")
print("Normal termination")