def findno(x):
    if x%2 == 0:
        return ('Even')
    else:
        return ('odd')
a=int(input('Enter a number: '))
grate=findno(a)
print('No:',grate)