'''
进程模型
'''

import os

print('process %s is  running ...' % os.getpid())

print('start fork child process ....')

name = 'zero'

# Unix/Linux操作系统提供了一个fork()系统调用,调用一次返回两次
# 当程序执行到fork()这句时候，已经开始进程的新建了，
# 它的新建是将父进程的状态，代码，等资源复制一份成一个新的进程，
# 代码执行进度也和父进程一样，
# 当fork执行完了的时候，已经成为了两个进程，
# 子进程返回的是0，父进程的fork返回的是子进程的pid
pid = os.fork()

# 打印fork之前的变量
print(name)
# 获取当前进程ID
print(os.getpid())

# multiprocessing 模块就是跨平台版本的多进程模块
from multiprocessing import Process

# 子进程要执行的代码
def run_process(name):
    print('the process is running  %s:%s ' % (name, os.getpid()))


if __name__ == '__main__':
    # 创建一个Process进程实例
    p = Process(target=run_process, args=('test',))
    print('the child process will start')
    # 用start()方法启动
    p.start()
    # join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步
    p.join()
    print('the child process is end')