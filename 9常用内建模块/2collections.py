# 一.namedtuple
# 我们知道tuple可以表示不变集合，例如，一个点的二维坐标就可以表示成：
# >>> p = (1, 2)
# 但是，看到(1, 2)，很难看出这个tuple是用来表示一个坐标的。
# 定义一个class又小题大做了，这时，namedtuple就派上了用场：

from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p)
print(p.x)
print(p.y)
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

# 二.deque

# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低。
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈：
from collections import deque
q = deque(['y','z','m',])
q.append('r')
q.appendleft('l')
print(list(q))
q.pop()
print(list(q))
q.popleft()
print(list(q))


# 三.defaultdict
# 使用dict时，如果引用的Key不存在，就会抛出KeyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict
d = defaultdict(lambda:'N/A')
d['key1'] = 'joey'
print(d['key1']) # exist
print(d['key2']) # not exist => N/A

# 四.OrderedDict
# 使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
# 如果要保持Key的顺序，可以用OrderedDict;
from collections import OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
 # d # dict的Key是无序的
# {'a': 1, 'c': 3, 'b': 2}
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
# od # OrderedDict的Key是有序的
OrderedDict([('a', 1), ('b', 2), ('c', 3)])

# 注意，OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
# >>> od = OrderedDict()
# >>> od['z'] = 1
# >>> od['y'] = 2
# >>> od['x'] = 3
# >>> list(od.keys()) # 按照插入的Key的顺序返回
# ['z', 'y', 'x']
# OrderedDict可以实现一个FIFO（先进先出）的dict，当容量超出限制时，先删除最早添加的Key：


# 五.Counter

# Counter是一个简单的计数器，例如，统计字符出现的个数：

from collections import Counter
c =  Counter()
for ch in 'Programming':
    c[ch] = c[ch]+1
print(c)
# Counter({'r': 2, 'g': 2, 'm': 2, 'P': 1, 'o': 1, 'a': 1, 'i': 1, 'n': 1})
# Counter实际上也是dict的一个子类，上面的结果可以看出，字符'g'、'm'、'r'各出现了两次，其他字符各出现了一次。

