# Enum

from enum import Enum, unique

Month = Enum ('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
print (Month.Jan)
for name, menber in Month.__members__.items ():
    print (name, '=>', menber, ',', menber.value)


# value属性则是自动赋给成员的int常量，默认从1开始计数。
# 如果需要更精确地控制枚举类型，可以从Enum派生出自定义类：

@unique
class Weekday (Enum):
    Sun = 0,
    Mon = 1,
    Tus = 2,
    Wed = 3,
    Thu = 4,
    Fri = 5,
    Sat = 6
day1 = Weekday.Mon #Weekday['Mon']  Weekday.Tue.value  Weekday(1)
print(day1)















