n=int(input('enter range: '))
print('Even Natural Numbers between 1 to', n,': ')
for i in range(2,n+1,2):
    print(i,end=' ')
print('\nOdd Natural Numbers between 1 to', n,': ')
for i in range(1,n+1,2):
    print(i,end=' ')