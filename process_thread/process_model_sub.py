'''
很多时候，子进程并不是自身，而是一个外部进程。
我们创建了子进程后，还需要控制子进程的输入和输出。
'''

# subprocess模块可以让我们非常方便地启动一个子进程，然后控制其输入和输出。

import subprocess

print('ps -aux')
# 查询进程
r = subprocess.call(['ps',"aux"])



print(r)
