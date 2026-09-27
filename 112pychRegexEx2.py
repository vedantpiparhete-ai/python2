import  re
text="python is very useful and powerful language"
pattern='Python'
result=re.match(pattern,text)
# print(result.group())
if result:
    print("Pattern found: ",result.group())
else:
    print("Pattern not found")