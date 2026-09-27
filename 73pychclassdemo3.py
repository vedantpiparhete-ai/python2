class Animal:
    def setdetail(self,colour,age,name):
        self.colour=colour
        self.age=age
        self.name=name

    def display(self):
        print(f'Colour of dog: {self.colour}')
        print(f'Age of dog: {self.age}')
        print(f'Name of dog: {self.name}')

roxi=Animal()
roxi.setdetail('white',5,'Roxie')
roxi.display()
Luci=Animal()
Luci.setdetail('GoldenWHite',3,'Luci')
Luci.display()
