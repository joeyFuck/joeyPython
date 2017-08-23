import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

# Hello world! (<_MainThread(MainThread, started 47488)>)
# Hello world! (<_MainThread(MainThread, started 47488)>)
# Hello again! (<_MainThread(MainThread, started 47488)>)
# Hello again! (<_MainThread(MainThread, started 47488)>)
# 两个Task，可看到，第一个Task，执行到asyncio.sleep(1)，并未阻塞在这里，而是中断，等待返回值，同时处理第二个Task，
# 所以是两个Hello world先输出。再有，可看到输出两个Hello world的线程均为47488（每次不同），所以又验证该线程未阻塞。

# 效率上，简单来看，提高一倍（忽略打印helloeworld的时间，主要是sleep的一秒钟）

# 异步操作需要在coroutine中通过yield from完成；（相当于把耗时操作搞成异步操作，然后这个异步操作需通过yield from完成）
#
# 多个coroutine可以封装成一组Task然后并发执行。










