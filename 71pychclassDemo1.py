class  student:
    #Memebers of Class
    name='Vedant'
    roll=121

    def display(self):
        print('Name: ',self.name)
        print('Roll number: ',self.roll)

#Object Creation
s1=student()
s1.display()
s2=student()
s2.roll=122
s2.name='Venkatesh'
s2.display()