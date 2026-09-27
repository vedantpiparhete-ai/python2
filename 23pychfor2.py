n=int(input('enter range: '))
print('First ',n,'natural number: ')
print('Ascending: ')
for i in range(1,n+1):
    print(i,end=' ')
print('\nDescending: ')
for i in range(n,0,-1):
    print(i,end=' ')