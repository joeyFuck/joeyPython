class Animal(object):
    def __init__(self,name):
        self.name = name  #这里相当于新增了一个属性name
    def run(self):
        print(self.name+' is running')
class Cat(Animal):
    pass
class Dog(Animal):
    pass
a = Cat('cat')
a.run()
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，这就是多态真正的威力：
# 调用方只管调用，不管细节，
# 而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：
#
# 对扩展开放：允许新增Animal子类；
#
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
def runTwice(animal):
    animal.run()
    animal.run()
runTwice(Animal('animal'))
runTwice(Cat('cat'))
runTwice(Dog('dog'))

