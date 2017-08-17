# 在绑定属性时，如果我们直接把属性暴露出去，虽然写起来很简单，但是，没办法检查参数，导致可以把成绩随便改：
class Student(object):
    pass
s = Student()
s.score = 90
print(s.score)
s.score = 900
# 这显然不合逻辑。为了限制score的范围，可以通过一个set_score()方法来设置成绩，
# 再通过一个get_score()来获取成绩，这样，在set_score()方法里，就可以检查参数：

class Stu(object):
    def get_score(self):
        return  self.score
    def set_score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger')
        if value < 0 or value > 100:
            raise  ValueError('score must between 0~100')
        self.score = value
s1 = Stu()
s1.set_score(100)
print(s1.get_score())
# 但是，上面的调用方法又略显复杂，没有直接用属性这么直接简单。

# 有没有既能检查参数，又可以用类似属性这样简单的方式来访问类的变量呢？对于追求完美的Python程序员来说，这是必须要做到的！
# 还记得装饰器（decorator）可以给函数动态加上功能吗？对于类的方法，装饰器一样起作用。
# Python内置的@property装饰器就是负责把一个方法变成属性调用的：

# 注意：方法score作为属性调用，此时，方法内部的属性应为_score 可以理解为私有字段

class Stu2(object):
    @property
    def score(self):
        return  self._score

    @score.setter
    def score(self,value):
        if not isinstance(value,int):
            raise ValueError('score must be an interger')
        if value < 0 or value > 100:
            raise  ValueError('score must between 0~100')
        self._score = value
s2 = Stu2()
s2.score = 10
# s2._score = 110 # 此时，由于我们的“私有字段”_score跟方法score挂钩，实例使用中，不应再动态新增属性_score,不然会造成_score值的覆盖
print(s2.score)
print(s2._score)

# 还可以定义只读属性，只定义getter方法，不定义setter方法就是一个只读属性：














