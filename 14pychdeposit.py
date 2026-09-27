bal= 80000
pin = int(input('Enter PIN: '))
if pin == 270507:
    print('we are Well comeing you Vedant')
    print('Balance: ', bal)
    print('--------------------------------------------')
    amt=int(input('Enter Amount to deposit: '))
    if amt > 100000:
        print(' Amount cannot be greater than 100000 ')
    if amt < 0:
        print('Invalid Amount')
    elif amt <= bal:
        bal=bal+ amt
        print(amt,'/- Deposited Successfully')
        print('Avl.Bal: ',bal)
else:
    print('Invalid PIN')