'''
进程间通信
可以使multiprocessing里面的Queue,Pipes等多种方式来交互数据
'''

from  multiprocessing import Process, Queue
import os, random, time

# 读数据进程执行的代码:
def read(q):
    while True:
        print('start waiting data arrive...')
        value = q.get(True)
        print('the value is %s' % value)

# 写数据进程执行的代码:
def write(q):
    print('start write data ...')
    for x in ['a', 'b', 'c']:
        print('wirting data %s' % x)
        q.put(x)
        time.sleep(random.randint(4,10))


if __name__ == '__main__':
    print("start queue test")
    # 创建队列
    q = Queue()

    # 创建进程
    w = Process(target=write,args=(q,))
    r = Process(target=read,args=(q,))
    # 启动子进程
    w.start()
    r.start()

    # 等待w结束:
    w.join()

    # 进程里是死循环，无法等待其结束，只能强行终止:
    r.terminate()

