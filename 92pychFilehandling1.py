'''
variable --> to store data
File -->
twp type
1)Text File -- pdf, txt , doc
2)Binary File -- jpg, mp4, gft
----------------------------------------
mode --->
1)a----->write
2)r----->read
3)e----->append
'''


f=open('Text File.txt','w')  # a is for writing everything in same line and of \n put the another line in different line
f.write('Welcome to the file \n') # w puts everything in proper maner it does not repet same line and after \n it puts line in another line
f.write('This is our first file.')
print('File created and data stored')



lines=['Hello\n', 'Welcome\n', 'Here in python world\n']
f1=open('Text File2.txt','a')
f1.writelines(lines)
f1.close()
f.close()
