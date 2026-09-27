from ctypes import c_int16

class Dog:
    def sound (self):
        print('Dog Barks(Bhow Bhow) ')

class Cat:
    def sound (self):
        print('Cat Meows(Meow Meow go----- ) ')

class Cow:
    def sound (self):
        print('Cow (Mow Mow ) ')

def make_sound(animal):
    animal.sound()

d1=Dog()
c1=Cat()
m1=Cow()
make_sound(d1)
make_sound(c1)
make_sound(m1)