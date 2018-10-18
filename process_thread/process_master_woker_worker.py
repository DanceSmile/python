'''

'''
import time
from multiprocessing.managers import BaseManager

class ManagerQueue(BaseManager):
    pass

ManagerQueue.register('get_task_queue')
ManagerQueue.register('get_result_queue')

m = ManagerQueue(address=('', 5000), authkey=b'abc')
m.connect()

task = m.get_task_queue()
result = m.get_result_queue()


for i in range(10):
    try:
        n = task.get(timeout=1)
        time.sleep(2)
        result.put(n)
    except Exception as e:
        print(e)

print('worker exit.')

