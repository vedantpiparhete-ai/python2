l1=[10,20,30,40,30,20,10]
print(l1.index(40))
print(l1.index(40,3))
print(l1.count(10))
l2=[1,3,5,6,7,2,4,]
l2.sort()
print(l2)
l2.sort(reverse=True)
print(l2)
l3=['Banana','apple','mango']
l3.sort(key=str.lower) #case insensitive
print(l3)
l3.sort(key=str.lower,reverse=True)#reverse has done and in lower case
print(l3)


c1=[10,20,30,40]
c2=[]
c2 = c1.copy()
print(c2)
c1.append(50)#in this if one time you have done copy then you cant do again
print(c1)
print(c2)