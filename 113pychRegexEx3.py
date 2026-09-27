import re
text="aa bb aaa bbb aa aa bbbccc aaa baaa cc"
text1='python is best language and no one can bet python aaa'
result=re.findall(text,text1)
print(result)