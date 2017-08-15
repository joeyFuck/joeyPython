# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
#一、 使用type()

print(type(123))
print(type('str'))

b = type(123)==type(456)
print(b)
b = type(123) == int
print(b)
b = type(123) == type('str')
print(b)
# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：

import  types
def Fn():
    pass
b = type(Fn) == types.FunctionType
print(b)
b = type(abs)==types.BuiltinFunctionType
print(b)
b =  type(lambda x: x) == types.LambdaType
print(b)
b = type((x for x in range(10))) == types.GeneratorType
print(b)
print(list(x for x in range(10)))
print(list(x*x for x in range(10)))

# 二、 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

class Animal(object):
    pass

class Cat(Animal):
    pass

joey = Cat()
b = isinstance(joey,Cat)
print(b)
b = isinstance(joey,Animal)
print(b)
# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
b = isinstance([1,2,3],(list,tuple))
print(b)
b = isinstance((1,2,3),(list,tuple))
print(b)
b = isinstance('ss',(int,str))
print(b)

# 三、 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('str'))
# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。在Python中，如果你调用len()函数试图获取一个对象的长度，
# 实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

print(len('123'))
print('123'.__len__())

# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：
class MyCat(object):
    y = 10
    def __len__(self):
        return 100
print(len(MyCat()))
print(MyCat().__len__())

b = hasattr (MyCat, 'x')  # 有属性'x'吗？
print(b)
b = hasattr (MyCat, 'y')  # 有属性'x'吗？
print(b)
print(MyCat.y)
setattr(MyCat, 'x', 19) #动态添加一个属性x
print(MyCat.x)

getattr(MyCat, 'z', 404) # 获取属性'z'，如果不存在，返回默认值404  404是我们传的默认值，可以改为其他。

# 一个正确的用法的例子如下：

def readImage(fp):
    if hasattr(fp, 'read'):
        return readData(fp)
    return None
# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，如果存在，则该对象是一个流，
# 如果不存在，则无法读取。hasattr()就派上了用场。
#
# 请注意，在Python这类动态语言中，根据鸭子类型，有read()方法，不代表该fp对象就是一个文件流，它也可能是网络流，
# 也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。











