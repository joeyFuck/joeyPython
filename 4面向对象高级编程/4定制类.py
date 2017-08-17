# __str__
class Student(object):
    def __init__(self,name):
        self.name  = name
print(Student('joey'))

# 打印出一堆<__main__.Student object at 0x109afb190>，不好看。
# 怎么才能打印得好看呢？只需要定义好__str__()方法，返回一个好看的字符串就可以了：
class Stu1(object):
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return  'Stu object (name: %s)' % self.name
print(Stu1('joeyFuck'))

# __iter__ 相当于迭代器
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，
# 然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
# 注意点，不能像list一样用下标取值Fib()[5] TypeError: 'Fib' object does not support indexing
class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1# 初始化两个计数器a，b
    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己
    def __next__(self):
        self.a,self.b = self.b,self.a + self.b
        if self.a > 1000: #退出的条件
            raise StopIteration()
        return self.a
for x in Fib():
    print(x)

# __getitem__() 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f1 = Fib1()
print(str(f1[3])+'```````````````````````````````````')

class Fib2(object):
    def __getitem__(self, n):
        if isinstance(n, int): # n是索引
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice): # n是切片
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L
f2 = Fib2()
print(f2[5:10])
print(f2[:10])
print('--------------------------------------------------------------------------------------------')

# __call__
# 让实例本身作为函数使用
# __call__()还可以定义参数。
# 对实例进行直接调用就好比对一个函数进行调用一样，所以你完全可以把对象看成函数，把函数看成对象，因为这两者之间本来就没啥根本的区别。
class Stu2(object):
    def __init__(self,name):
        self.name = name
    def __call__(self, *args, **kwargs):
        print('my name:%s' % self.name)
s = Stu2('joey')
s() #实例当函数使用

# 很多的时候，我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
b = callable([1, 2, 3])
print(b)
b = callable(Stu2('jj'))
print(b)
b = callable(max)
print(b)
b = callable(Student('mm'))
print(b)

























