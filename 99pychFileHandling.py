# with open('Text File6.txt','w') as f:
#     for i in range(1,4):
#         print(f'Enter Details of Students : {i}')
#         id = input('Enter Student ID : ')
#         name = input('Enter Student Name : ')
#         course = input('Enter Student Course Name : ')
#         city = input('Enter Student City Name : ')
#         print('----------------------------------------------')
#         f.write(id)
#         f.write('\t')
#         f.write(name)
#         f.write('\t')
#         f.write(course)
#         f.write('\t')
#         f.write(city)
#         f.write('\n')


with open('Text File6.txt','w') as f:
    for i in range(1,4):
        print(f'Enter Details of Students : {i}')
        id = input('Enter Student ID : ')
        name = input('Enter Student Name : ')
        course = input('Enter Student Course Name : ')
        city = input('Enter Student City Name : ')
        print('----------------------------------------------')
        f.write(id)
        f.write('\t')
        f.write(name)
        f.write('\t')
        f.write(course)
        f.write('\t')
        f.write(city)
        f.write('\n')
