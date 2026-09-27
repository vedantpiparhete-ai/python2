number =' '
count = 0
even = 0
odd = 0
while True:
    #number!=0:
    #number != 'exit': --- no need in this:
    number = int(input('Enter any number: '))
    if number == 0:
        break
    if number % 2 == 0:
        even += 1
        #even = even + 1
    else:
        odd += 1
        #odd = odd + 1
print('--------------------------------------')
print('Program Terminated ')
#print('Total Number added: ', count + 1) --- not mendatery
print('Total Even Number added: ', even)
print('Total Odd Number added: ', odd)