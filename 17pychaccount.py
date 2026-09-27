pin=int(input('Enter Pin: '))
if pin == 2705:
    print('You are Welcome')
    print('------------------------------')
    print('Select Sections')
    print('w--> Withdraw')
    print('d--> Deposit')
    print('b--> Balance')
    print('e--> Current Balance')
    print('------------------------------')
    choice=input('Enter your choice: ')
    print('------------------------------')
    match choice:
        case 'w':
            bal=100000
            print('Withdraw the Amount')
            withdraw = int(input('Enter your withdraw amount: '))
            if withdraw <= 0 or withdraw >= bal:
                print('Invalid Amount')
            elif withdraw <= bal:
                print('Avl.bal: ',bal - withdraw)
            else:
                print('in sufficient balance')

        case 'd':
            bal=100000
            print('Withdraw the Amount')
            amount=int(input('Enter your deposit amount: '))
            if amount<=0 or amount>=bal:
                print('Invalid Amount')
            elif amount<0:
                print('Not possible ,Please Deposit less than 100000')
            elif amount<=bal:
                bal=bal+amount
                print(amount,'/-credited Successfully')
                print('Avl.bal: ',bal)

        case 'b':
            bal=100000
            print('Your Current Balance: ',bal)

        case 'e':
            bal=100000
            print('Your Current Balance: ',bal)

        case _:
            print('Invalid Choice')

else:
    print('Invalid Choice')
    print('Enter your choice Correct Pin: ')
    print('Thank for your balance')