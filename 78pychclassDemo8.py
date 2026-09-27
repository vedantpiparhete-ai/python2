'''
1)Local variable : Any variable defined inside any variable block like method ,loop etc.
2)Global variable : There variable are defined outside the class method ,or we can also define using global keywords
3)Instance variable : These variable varies from object to object.
it also creates a seprate copy of variable from every object.
4)Class variable : IT will create a single copy which will be shared with every object
it does not varry from object to object.
'''

class Test:
    common = 120

    def m1(self,x,y):
        self.x=x
        self.y=y

    def m2(self):
        print("X= ",self.x)
        print("Y= ",self.y)

t1=Test()
t1.m1(10,20)
t1.m2()
print(t1.common)
t2=Test()
t2.m1(10,20)
t2.m2()
print(t2.common)