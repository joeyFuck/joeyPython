#filter()函数返回的也是一个Iterator，也就是一个惰性序列，所以要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list
#貌似只是用来筛选，不能对序列进行值的改变
def is_joey(name):
    if name == 'joey':
         return str(name).upper()
        # return  True
    return  False
l = list(filter(is_joey,['jj','bob','joey','mary']))
print(l)
