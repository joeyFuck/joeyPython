# Python提供了pickle模块来实现序列化。
import pickle
d = dict(name='joey', age = 20, score = 80)
b = pickle.dumps(d) # pickle.dumps()方法把任意对象序列化成一个bytes
print(b)

with open('../data/dump.txt', 'wb') as f:
    pickle.dump(d,f)
with open('../data/dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：

# json对dict进行序列化与反序列
import json
d = dict(name='Bob', age=20, score=88)
json_res = json.dumps(d)
print(json_res)

# 类似的，dump()方法可以直接把JSON写入一个file-like Object。
# json.dumps -- json.loads,json.dump -- json.load
# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
obj = json.loads(json_res)
print(obj)



# json对类对象进行序列化与反序列
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(stu):
    return {
        'name':stu.name,
        'age': stu.age,
        'score': stu.score
    }
s = Student('joey','18','100')
print(json.dumps(s, default=student2dict))
# 不过，下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s,default=lambda x:x.__dict__))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。

# json 反序列化 同样的道理，如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook=dict2student))





















