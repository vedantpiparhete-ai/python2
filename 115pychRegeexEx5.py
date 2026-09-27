import re
pattern=r'[a-z,0-9]'
data='todat is my seek day with worke day so i spend 1000 on it'
match=re.findall(pattern,data)
print(match)