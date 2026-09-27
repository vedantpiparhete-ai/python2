class Circle:

    def calculate(self,radius):
        self.radius=radius

    def calare(self):
        return 3.14*self.radius**2

    def calcir(self):
        return 2*3.14*self.radius

c1=Circle()
c2=Circle()
c1.calculate(5)
c2.calculate(8)

print('Circle1: ')
print(f'Area of circle: {c1.calare()}')
print(f'Circumference of circle: {c1.calcir()}')
print('Circle2: ')
print(f'Area of circle: {c2.calare()}')
print(f'Circumference of circle: {c2.calcir()}')