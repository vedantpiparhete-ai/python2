s1={'apple','mango','banana'}
s1.add('papaya')
print(s1)
s1.discard('Apple')
print(s1)
l1=['potato','tomato']
s1.update(l1)
print(s1)
s1.pop()
print(s1)
s2=s1.copy()
print(s2)

print('------------------------------------------------------------------------------')
a={10,20,30}
b={20,40,50}
print(f'union {a.union(b)}')
print(f'Intersection {a.intersection(b)}')
print(f'Difference {a.difference(b)}')
print(f'Difference {a.difference(a)}')
print(f'Symmetric Difference {a.symmetric_difference(b)}')
print(f'Is subset {a.issubset(b)}')
print(f'Is superset {a.issuperset(b)}')
print(f'Is Disjoint {a.isdisjoint(b)}')

print('\n------------------------------------------\n')

s={400,500,300,200,100}
s.add(11)
s=frozenset(s)
#s.add(111)  -- it will not added and it will give error in the code
print(s)