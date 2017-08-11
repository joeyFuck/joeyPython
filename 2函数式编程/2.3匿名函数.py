# 匿名函数
# 关键字lambda表示匿名函数，冒号前面的x表示函数参数。
l = list(map(lambda x:x*x,[1,3,4,5,2,7]))
print(l)
# 用匿名函数有个好处，因为函数没有名字，不必担心函数名冲突。此外，匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数：
fn = lambda x,y:x+y
print(fn(1,5))
# 同样，也可以把匿名函数作为返回值返回
def build(x,y):
    return  lambda :x*y
print(build(8,9)())