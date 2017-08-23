#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Joey zhu'

#一、读文件

# 读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
f = open('../data/test.txt', 'r', encoding='UTF-8')  # 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
print(f.readline()) #f.read()
f.close()

# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件，我们可以使用try ... finally来实现：
try:
    f = open ('../data/test.txt', 'r', encoding='UTF-8')
    print (f.readline())
finally:
     f.close ()
# 但是每次都这么写实在太繁琐，所以，Python引入了with语句来自动帮我们调用close()方法：
with open('../data/test.txt', 'r', encoding='UTF-8') as f:
    # for line in f.readlines():
    #     print(line.strip()) # 把末尾的'\n'删掉
    print(f.read(5)) # 5个字 10字节？

# file-like Object

# 像open()函数返回的这种有个read()方法的对象，在Python中统称为file-like Object。
# 除了file外，还可以是内存的字节流，网络流，自定义流等等。file-like Object不要求从特定类继承，只要写个read()方法就行。
#
#StringIO就是在内存中创建的file-like Object，常用作临时缓冲。


# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。
# 遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：

with open('../data/test.txt', 'r', encoding='UTF-8', errors='ignore') as f:
    print(f.read(10))

# 二、写文件

# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# import PIL.Image as pic
# pic1 = pic.open('G:\zzz.jpg')
# pic1.show()

# w wb(字节) a(追加)
# with open('../data/test.txt','w',encoding='UTF-8',errors='ignore') as f:
#     f.write('joey is good')

with open('../data/test.txt','a',encoding='UTF-8',errors='ignore') as f:
    f.write('joey is good')
























