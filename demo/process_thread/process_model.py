'''
进程模型


'''

import os

print('process %s is  running ...' % os.getpid())

print('start fork child process ....')

pid = os.fork()


print(os.getppid())


from multiprocessing import Process

def run_process(name):
    print('the process is running  %s:%s ' % (name, os.getpid()))


if __name__ == '__main__':

    p = Process(target=run_process, args=('test',))
    print('the child process will start')
    p.start()
    p.join()
    print('the child process is end')