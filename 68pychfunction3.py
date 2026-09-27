def per(b):
    if b > 100 or b < 0:
        return print("Invalid input")
    elif b >= 35:
        return print("Pass")
    else:
         return print("Fail")

a=int(input("Enter your percent: "))
Result=per(a)