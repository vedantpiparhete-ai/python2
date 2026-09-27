bal= 80000
pin = int(input('Enter PIN: '))
if pin == 270507:
    print('Wellcome to Vedant')
    print('Balance: ', bal)
    print('--------------------------------------------')
    amt=int(input('Enter Amount: '))
    if amt < 0:
        print('Invalid Amount')
    elif amt <= bal:
        bal=bal-amt
        print(amt,'/- Debited Successfully')
        print('Avl.Bal: ',bal)
    else:
        print('Invalid Amount')
else:
    print('Invalid PIN')