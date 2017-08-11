def now():
    print('2017-08-10')
f = now
f()
print(f.__name__)
# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，
# 这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。

def log(func):
    def wrapper(*args, **kw):
        print('%log--start%')
        func(*args,**kw)
        print('%log--end%')
    return  wrapper;

# 使用方法一
log(f)()

# 使用方法二
@log
def logFun():
    print('装饰器测试')
logFun()
# 把@log放到logFun()函数的定义处，相当于执行了语句：
# logFun = log(logFun)
# 因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'logFun'变成了'wrapper'：
print(logFun.__name__)
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：
import functools
def log2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('%log--start%')
        func(*args,**kw)
        print('%log--end%')
    return  wrapper;
@log2
def logFun2():
    print('装饰器测试--functools.wraps')
print(logFun2.__name__)

# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。
# OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。
# Python的decorator可以用函数实现，也可以用类实现。
