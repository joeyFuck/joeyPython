import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
# 这就是logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。这样一来，你可以放心地输出不同级别的信息，
# 也不用删除，最后统一控制输出哪个级别的信息。
# logging的另一个好处是通过简单的配置，一条语句可以同时输出到不同的地方，比如console和文件。


# pdb
# 调试
# ide调试

# 虽然用IDE调试起来比较方便，但是最后你会发现，logging才是终极武器。






