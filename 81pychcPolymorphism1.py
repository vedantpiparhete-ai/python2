# print(2+2)--sum
# print('2'+'2')--concatination
# we can overload
# 1)method (not allowed in python)
# 2)Operator (allowed in python)
# 3)Constructor (not allowed in python)
#
# def add(a,b):
#     print(a+b)
#
# def add(a,b,c):
#     print(a+b+c)
#
# add(10,20,)
#add(10,20,30)

#Python does not support overloding of method directly

class PolyDemo:

    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

p1= PolyDemo()
print(p1.add(10,20,30))