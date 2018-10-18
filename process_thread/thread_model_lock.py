'''
lock
线程之间共享数据 锁
'''
import threading

balance = 0
lock = threading.Lock()

def change_it(x):
    global balance
    balance = balance+x
    balance = balance-x

def run_thread(n):
    for i in range(10000):
        # 锁住
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()



t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(10,))
t1.start()
t2.start()
t1.join()
t2.join()

print('all thread done')
print('result: %s' % balance)

