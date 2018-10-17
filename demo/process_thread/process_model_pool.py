

from multiprocessing import Pool
import os, time, random

def run_poll_process():
    print('the child process running %s' % os.getpid() )
    time.sleep(random.randint(2,6))

    print('the child process %s done' % os.getpid() )


print('the main process is %s' % os.getpid() )
p = Pool(4)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)
p.apply_async(run_poll_process)

p.close()
p.join()
print('the all process done')
