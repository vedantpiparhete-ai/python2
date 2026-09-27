import re
data='Vedant got 90 marks and Gauri got 80'
data1='a aa aaa aaaa aaaaa'
data2='color  colour colouur'
data3='Mr Piparhete and Mrs Piparhete are Invited'
data4='colorr  colourr colouurrr'
pincode=['440032','440023','440009','440024','8308227447']
pattern=r'[\d*]'
pattern1=r'[\d*]'
print(re.findall(r'\d+',data))
print(re.findall(r'a',data1))
print(re.findall(r'colou?r',data2))
print(re.findall(r'Mrs?',data3))
print(re.findall(r'colou?r?',data4))
#Getting valid pins
for pins in pincode:
    if re.findall(r'\d{6}',pins):
        print(pins,'Valid')
    else:
        print(pins,'Invalid')