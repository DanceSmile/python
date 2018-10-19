'''
操作文件和目录
'''

import os

# 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
r = os.name

# 系统详情
r = os.uname()
# posix.uname_result(sysname='Darwin', nodename='MichaelMacPro.local', release='14.3.0', version='Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64', machine='x86_64')

# 系统环境变量
r = os.environ
# environ({'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin', 'PYTHONPATH': '/Applications/PyCharm.app/Contents/helpers/pycharm_matplotlib_backend:/Users/dancesmile/Desktop/python', 'SHELL': '/bin/zsh', 'PAGER': 'less', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'PYTHONIOENCODING': 'UTF-8', 'OLDPWD': '/Applications/PyCharm.app/Contents/bin', 'USER': 'dancesmile', 'ZSH': '/Users/dancesmile/.oh-my-zsh', 'TMPDIR': '/var/folders/00/v58n_v4x4v38z0h96c5qybzh0000gn/T/', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.LDxGsF4p4T/Listeners', 'XPC_FLAGS': '0x0', 'PYTHONUNBUFFERED': '1', '__CF_USER_TEXT_ENCODING': '0x1F5:0x0:0x0', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.jI3u9JU7qQ/Render', 'LESS': '-R', 'LOGNAME': 'dancesmile', 'LC_CTYPE': 'UTF-8', 'XPC_SERVICE_NAME': 'com.jetbrains.pycharm.2028', 'PWD': '/Users/dancesmile/Desktop/python/io_action', 'PYCHARM_HOSTED': '1', 'HOME': '/Users/dancesmile', 'PYCHARM_MATPLOTLIB_PORT': '59137', '__PYVENV_LAUNCHER__': '/usr/local/bin/python3.7'})
# 单独获取环境变量的值
r = os.environ.get('PATH')
# /usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin

# 查询当前文件夹的绝对路径
r = os.path.abspath('.')
# /Users/dancesmile/Desktop/python/io_action

# 把两个路径合成一个时，不要直接拼字符串
# 而要通过os.path.join()函数
# 这样可以正确处理不同操作系统的路径分隔符
r = os.path.join('test','dir')
# test/dir

# 创建文件夹
# r = os.mkdir('testdir')
# None

# 删除文件夹
# r = os.rmdir('testdir')
# None

# 拆分文件夹和文件
r = os.path.split('/foo/bar/f')
# ('/foo/bar', 'f')

# 提取后缀
r = os.path.splitext('/foo/bar/f.tet')
# ('/foo/bar/f', '.tet')

# 文件重命名
# os.rename('test.txt', 'test.py')
# 删除文件
# os.remove('test.py')

# 文件列表
r = os.listdir('.')

# 文件筛选
r = [ f for f in os.listdir('.')]
print(r)