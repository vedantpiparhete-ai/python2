d={101:'A',102:'B',104:'C'}
print(d)
d1=dict(Name='Vedant',City='Nagput')
print(d1)
print(d1['Name'])
print(d1['City'])
print(d1.get(101))
print(d1.get('Name'))
d1['Name']='Gauri'
print(d1)
d1['College']= 'S.B.Jain'
print(d1)
d1['College']='K.D.K'
print(d1)
del d1['College']
print(d1)
rem=d1.pop('Name')
print(rem," removed")