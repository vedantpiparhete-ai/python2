def findGrate(x,y):
    if x>y:
        return x
    else:
        return y

a=int(input('Enter first number: '))
b=int(input('Enter second number: '))
grate=findGrate(a,b)
print('Gratest No. : ',grate)