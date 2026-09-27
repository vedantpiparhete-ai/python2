import  re
text="python is very useful and powerful language"
pattern='language'
result=re.search(pattern,text)
print(result.group())
if result:
    print("Pattern found: ",result.group())
else:
    print("Pattern not found")