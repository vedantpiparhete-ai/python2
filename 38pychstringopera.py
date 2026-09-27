a = 'Python programing'
b = 'notes.pdf'
print(a.startswith('Python'))
print(b.endswith('pdf'))
c = 'admin123'
print(c.isalnum())
c = 'admin'
print(c.isalpha())
d = '123456'
print(d.isdigit())
d = '  '
print(d.isspace())
e = 'hello'
print(e.islower())
e = ' HELLO'
print(e.isupper())
uname = ' vedant piparhete '
print(uname)
uname = uname.rstrip()
uname = uname.lstrip()
print(uname)
s='i love python'
print(s.replace('python','java'))
print(s)
fruits='apples, bananas, oranges'
l=fruits.split(',')
print(fruits)
print(fruits.split(','))
s='we are learning python and python is eassy to learn'
print(s.count('python'))
print('Hellow'.center(20,'*'))
print('121'.zfill(7))