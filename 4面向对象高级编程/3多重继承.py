# 分类类型不同，导致单继承的局限性。多继承在某个角度还是很方便的能解决的一些问题
class Animal(object):
    def run(self):
        print('i am animal')
class FlyAble(object):
    def fly(self):
        print('i can fly')

class RunAble (object):
    def fly(self):
        print ('i can run')
class Bird(Animal,FlyAble):
    pass
class Dog(Animal,RunAble):
    pass
# 通过多重继承，一个子类就可以同时获得多个父类的所有功能。
# C#中只有单继承，如上情况会通过FlyAble RunAble来继承Animal 然后Bird跟Dog来继承对应的RunAble或FlyAble。
# 那么多继承之于单继承的优点在哪儿呢，暂时理解，如以下场景，若一个animal即可run又可fly，那么单继承的实现只能新建一个class，即有flyAble，
# 又有runAble，然后这个animal继承此class。多继承直接继承两者即可。

# MixIn
# 在设计类的继承关系时，通常，主线都是单一继承下来的，例如，Ostrich继承自Bird。但是，如果需要“混入”额外的功能，
# 通过多重继承就可以实现，比如，让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。




















