import os   #引入模块

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1)
list2 = range(1, 11)
print(type(list2))
for x in list2:
    print(x)
print([x*x for x in range(1, 11)])
print([x*x for x in range(1, 11) if(x % 2 == 0)])
print([m + n for m in 'ABC' for n in 'XYZ'])

print([d for d in os.listdir('.')])

d = {'name':'joey', 'score': '100'}
for x, y in d.items():
    print(x+':'+y)

l=[k+'='+v for k, v in d.items()]
print(l)

print([s.upper() for s in l])

L1 = ['Hello', 'World',18, 'Apple',None]
print([x.lower() for x in L1 if(isinstance(x,str))])






















