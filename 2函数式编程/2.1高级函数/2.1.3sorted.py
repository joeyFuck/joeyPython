print(sorted([1,2,-33,-12,89,22]))
#sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
#同意也只是进行排序，不对值本身进行修改
print(sorted([1,2,-33,-12,89,22],key=abs))
print(sorted(['ca','bd','Sxa','ASC','lJm'],key=str.lower))