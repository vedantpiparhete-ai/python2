num=int(input('Enter 1 , 2 , 3 or 4: '))
match num:
    case 1:
        print('Good Morning')
    case 2:
        print('Good Afternoon')
    case 3:
        print('Good Evening')
    case 4:
        print('Good Night')
    case _:
        print('Good Bye')