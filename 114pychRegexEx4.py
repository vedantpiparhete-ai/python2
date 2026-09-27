import re
pattern=re.compile(r'ab',re.IGNORECASE)
data='abababababaaaabbb'
matches=re.finditer(pattern,data)
for m in matches:
    print(m.group())
    print('start: ',m.start())
    print('end: ',m.end())