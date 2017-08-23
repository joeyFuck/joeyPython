#高阶函数 higher order function
# 变量可以指向函数
l = abs(-10.123)
print(l)
joey = abs
print(joey(-5))

# 函数名只是个变量，abs是内置的函数名，如果手动将其指向其他对象，则变为其他变量
#abs = 10
#print(abs)
#print(abs(-10))#TypeError: 'int' object is not callable

#既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。

def add(x,y,f):
    return  f(x)+f(y)

print(add(1,-5,joey))

#有点类似C#的委托，函数做变量









































