from functools import reduce

# map
def f(x):
    return  x*x
print(list(map(f,[1,2,3,4,5,6])))
print([x for x in map(f,[1,2,3,4,5,6])])
print(list(map(str,[1,2,3,4,5,6,7])))

#reduce
#reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
def add(x,y):
    return x + y
print(reduce(add,[1,2,3,4,5,6]))
def fn(x,y):
    return  x*10+y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(reduce(fn,map(char2num,['1','2','5','9'])))













