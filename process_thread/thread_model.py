'''
thread
多线程和多进程最大的不同在于
多进程中，同一个变量，各自有一份拷贝存在于每个进程中，互不影响
而多线程中，所有变量都由所有线程共享
任何一个变量都可以被任何一个线程修改
线程之间共享数据最大的危险在于多个线程同时改一个变量
'''

import threading, time

# 线程函数
def loop():
    print('thread %s is running ...' % threading.current_thread().name)
    print('thread %s is done ...' % threading.current_thread().name)

print('thread %s is running ...' % threading.current_thread().name)
# 启动一个线程就是把一个函数传入并创建Thread实例，然后调用start()开始执行
t = threading.Thread(target=loop, name='loopThread')
# 启动线程
t.start()
# 等待线程结束
t.join()
print('thread %s is done ...' % threading.current_thread().name)


# 多线程同事修改数据

balance = 0

# 修改数据，正常执行流程应该一直为０
def change_it(n):
    global balance
    balance = balance+n
    balance = balance-n

def run_thread(change):
    for i in range(10000000):
        change_it(change)

# 创建启动线程
t1 = threading.Thread(target=run_thread, args=(4,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

# 打印结果
print(balance)
# 84

'''
原因是因为高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算：
balance = balance + n
也分两步：
计算balance + n，存入临时变量中；
将临时变量的值赋给balance。

由于x是局部变量，两个线程各自都有自己的x，当代码正常执行时：
初始值 balance = 0

t1: x1 = balance + 5 # x1 = 0 + 5 = 5
t1: balance = x1     # balance = 5
t1: x1 = balance - 5 # x1 = 5 - 5 = 0
t1: balance = x1     # balance = 0

t2: x2 = balance + 8 # x2 = 0 + 8 = 8
t2: balance = x2     # balance = 8
t2: x2 = balance - 8 # x2 = 8 - 8 = 0
t2: balance = x2     # balance = 0
结果 balance = 0

但是t1和t2是交替运行的，如果操作系统以下面的顺序执行t1、t2：
初始值 balance = 0
t1: x1 = balance + 5  # x1 = 0 + 5 = 5

t2: x2 = balance + 8  # x2 = 0 + 8 = 8
t2: balance = x2      # balance = 8

t1: balance = x1      # balance = 5
t1: x1 = balance - 5  # x1 = 5 - 5 = 0
t1: balance = x1      # balance = 0

t2: x2 = balance - 8  # x2 = 0 - 8 = -8
t2: balance = x2   # balance = -8

结果 balance = -8



'''

