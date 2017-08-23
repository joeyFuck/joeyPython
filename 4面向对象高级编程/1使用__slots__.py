class Student(object):
    pass

s = Student()
# 给实例绑定一个方法
def setAge(self,age):
    self.age = age #给实例绑定了一个属性

from types import MethodType
s.set_age = MethodType(setAge,s)# 给实例绑定一个方法
s.set_age(18)# 调用实例方法
print(s.age)# 测试结果

# 为了给所有实例都绑定方法，可以给class绑定方法：
def setScore(self,score):
    self.score = score
Student.set_score = setScore
s.set_score(90)
print(s.score)


# 动态绑定允许我们在程序运行的过程中动态给class加上功能，这在静态语言中很难实现。
# 但是，如果我们想要限制实例的属性怎么办？比如，只允许对Student实例添加name和age属性。

# 为了达到限制的目的，Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class实例能添加的属性：
class Teacher(object):
    __slots__ = ('name','gender')# 用tuple定义允许绑定的属性名称
t = Teacher()
t.name = 'joey'
t.gender = 'male'
print(t.name + ' is ' + t.gender)
# t.score = 90 报错

# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
# 除非在子类中也定义__slots__，这样，子类实例允许定义的属性就是自身的__slots__加上父类的__slots__。



