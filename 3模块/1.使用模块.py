#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""a test module"""

__author__ = 'Joey zhu'

import sys

def test():
    args = sys.argv
    if len(args) == 1:
        print('hello world,%s' % args[0])
    elif len(args) == 2:
        print('Hello,%s!' % args[1])
    else:
        print('Too much argument'+ args[2])

if __name__ == '__main__':
    test()

# 以上就是Python模块的标准文件模板，当然也可以全部删掉不写，但是，按标准办事肯定没错。






























