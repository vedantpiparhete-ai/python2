class Bank:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
                                            #__ this is super private & _ this is for only private

    def set_balance(self, balance):
        #validation
        self.__balance = balance

    def display(self):
        print("Name: ",self.name)
        print("Balance: ",self.__balance)

s1=Bank('Gauri',10000)
s1.display()
s1.set_balance(20000)
s1.display()

s2=Bank('VEDANT',100000)
s2.display()
s2.set_balance(200000)
s2.display()