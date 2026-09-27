'''
Method overriding : If you are not satisfied with parent class method implementation
That you can change the implementation in child class this concept is called as method
overriding.

'''

class animal:
    def sound (self):
        print('Sound Make by Animal: ')

class Dog(animal):
    def sound (self):
        print('Dog Barks(Bhow Bhow) ')

class Cat(animal):
    def sound (self):
        print('Cat Meows(Meow Meow go----- ) ')


m1=animal()
m1.sound()
d1=Dog()
d1.sound()
d2=Cat()
d2.sound()