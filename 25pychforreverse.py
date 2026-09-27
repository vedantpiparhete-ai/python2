a=int(input('Enter start value: '))
b=int(input('Enter end value: '))
print('Natural Numbers between ',a,' and ',b,' are')
if a<=b:
  for i in range(a, b+1):
    print(i, end=' ')
else:
    print('Natural Numbers between ',a,' and ',b,' are in reverse: ')
for i in range(a, b-1, -1):
    print(i, end=' ')
