# 其实操作系统提供的命令只是简单地调用了操作系统提供的接口函数，Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os
print(os.name) # 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数：
# print(os.uname())
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))

#操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：/
# 查看当前目录的绝对路径:
print(os.path.abspath('.'))
#  首先把新目录的完整路径表示出来: 不要用字符串拼接 而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
p = os.path.join('F:\joey\joeyPython', 'testdir')
print(p)
# 然后创建一个目录:
# os.mkdir(p)
# os.mkdir('F:/joey/joeyPython/testdir')
# 删掉一个目录:
# os.rmdir('F:/joey/joeyPython/testdir')

# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
# >>> os.path.split('/Users/michael/testdir/file.txt')
# ('/Users/michael/testdir', 'file.txt')
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
# >>> os.path.splitext('/path/to/file.txt')
# ('/path/to/file', '.txt')
# 这些合并、拆分路径的函数并不要求目录和文件要真实存在，它们只对字符串进行操作。
# 对文件重命名:
# >>> os.rename('test.txt', 'test.py')
# 删掉文件:
# >>> os.remove('test.py')

# 复制文件
# 但是复制文件的函数居然在os模块中不存在！原因是复制文件并非由操作系统提供的系统调用。理论上讲，我们通过上一节的读写文件可以完成文件复制，只不过要多写很多代码。
#
# 幸运的是shutil模块提供了copyfile()的函数，你还可以在shutil模块中找到很多实用函数，它们可以看做是os模块的补充。
#
# 最后看看如何利用Python的特性来过滤文件。比如我们要列出当前目录下的所有目录，只需要一行代码：

print([x for x in os.listdir('.') if os.path.isdir(x)])

# 要列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])






