'''
Pool: 进程池
如果要启动大量的子进程，可以用进程池的方式批量创建子进程：
'''
from multiprocessing import Pool
import os, time, random

# 子进程要执行的代码
def run_poll_process():
    print('the child process running %s' % os.getpid() )
    time.sleep(random.randint(2,6))
    print('the child process %s done' % os.getpid() )

print('the main process is %s' % os.getpid() )

# 一次最多执行５个进程
p = Pool(5)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)


# 对Pool对象调用join()方法会等待所有子进程执行完毕，
# 调用join()之前必须先调用close()，
# 调用close()之后就不能继续添加新的Process了
p.close()
p.join()
print('the all process done')


'''
the main process is 21479
the child process running 21484
the child process running 21485
the child process running 21486
the child process running 21488
the child process running 21487
the child process 21488 done
the child process running 21488
the child process 21486 done
the child process running 21486
the child process 21484 done
the child process running 21484
the child process 21487 done
the child process 21485 done
'''