'''
Inheritance(reusability)
to get property from one class to another class
The class  which gets provides is called as child class/ derived class for the class
which provide property is called as parent class or/ base class.
whatever belong to parent by default belong to child through inhertance.
Type:ta
Inheriance
`1)Single level inheritance --> one parent class and one child class
`2)Multilevel inheritance -->grandparent class to parent class to child class
`3)
`4)
`5)
`6)
'''

class P:
    def m1(self):
        self.bal=100000



class C(P):
    def m2(self):
        print('Balance',self.bal)


C1=C()
C1.m1()
C1.m2()