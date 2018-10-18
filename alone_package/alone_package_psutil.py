'''
psutil: process and system utilities
它不仅可以通过一两行代码实现系统监控，
还可以跨平台使用，支持Linux／UNIX／OSX／Windows等
是系统管理员和运维小伙伴不可或缺的必备模块。
'''

import os, psutil
# 2说明是双核超线程, 4则是4核非超线程
r = psutil.cpu_count() # CPU逻辑数量
# 4
r = psutil.cpu_count(logical=False) # CPU物理核心
# 2

# 统计CPU的用户／系统／空闲时间：
r = psutil.cpu_times()
# scputimes(user=12170.4, nice=503.6, system=6125.7, idle=231913.37, iowait=1051.56, irq=0.0, softirq=63.89, steal=0.0, guest=0.0, guest_nice=0.0)

# 使用psutil获取物理内存和交换内存信息，分别使用：
r = psutil.virtual_memory()
# svmem(total=8589934592, available=2866520064, percent=66.6, used=7201386496, free=216178688, active=3342192640, inactive=2650341376, wired=1208852480)
r = psutil.swap_memory()
# sswap(total=1073741824, used=150732800, free=923009024, percent=14.0, sin=10705981440, sout=40353792)

# 所有进程ID
r = psutil.pids()

# 获取指定的进程
p = psutil.Process(os.getpid())
# 获取进程名称
r = p.name()
# python3.6

# 进程exe路径
r = p.exe()
# /usr/bin/python3.6

# 进程的工作目录
r = p.cwd()
# /home/zero/python3-webapp/demo/alone_package

# 父进程ID
r = p.ppid()
# 11026

# 父进程
r = p.parent()
# psutil.Process(pid=11026, name='java', started='10:35:38')

# 进程启动的命令行
r = p.cmdline()
# ['/usr/bin/python3.6', '/home/zero/python3-webapp/demo/alone_package/alone_package_psutil.py']

# 子进程列表
r = p.children()
# []

# 进程状态
r = p.status()
# running

# 进程用户
r = p.username()
# zero

# 进程创建的时间
r = p.create_time()
# 1539832834.97

# 结束进程，自杀
p.terminate()
print(r)
