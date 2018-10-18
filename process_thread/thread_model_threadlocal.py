'''
ThreadLocal
一个ThreadLocal变量虽然是全局变量
但每个线程都只能读写自己线程的独立副本，互不干扰。
ThreadLocal解决了参数在一个线程中各个函数之间互相传递的问题。
'''

import threading

local_school = threading.local()

def process_school():
    std = local_school.student
    print(std)

def run_thread(name):
    local_school.student = name
    process_school()


t1 = threading.Thread(target=run_thread, args=('t1',))
t2 = threading.Thread(target=run_thread, args=('t2',))

t1.start()
t2.start()

t1.join()
t2.join()