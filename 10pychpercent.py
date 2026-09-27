per=int(input('Enter a Percentage: '))
if per> 100 or per<0:
    print("Invalid Percentage ")
elif per>89:
    print("A Grade Percentage ")
elif per>79:
    print("B Grade Percentage ")
elif per>69:
    print("C Grade Percentage ")
elif per>59:
    print("D Grade Percentage ")
elif per>49:
    print("E Grade Percentage ")
else:
    print("Fail Grade Percentage ")