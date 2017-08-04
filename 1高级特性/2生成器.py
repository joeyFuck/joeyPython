#generator
L = [x*x for x in range(10)]
print(L)
G = (x*x for x in range(10))
print(G)
#for x in G:
#    print(G.__next__())

#斐波拉契数列
def fib1(max):
    n,a,b = 0,0,1
    while(n<max):
        print(b)
        a,b = b,a+b
        n+=1
    return  'done'
#fib1(6)

#fib函数实际上是定义了斐波拉契数列的推算规则
#要把fib函数变成generator，只需要把print(b)改为yield b就可以了
def fib2(max):
    n,a,b = 0,0,1
    while(n<max):
        yield  b
        a,b = b,a+b
        n+=1
    return  'done'
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator
#调用generator fib2
g = fib2(6);
b = True;
while(b):
    try:
        x = next(g)
        print('g',x)
    except StopIteration as e:
        b = False
        print('g',e.value)



