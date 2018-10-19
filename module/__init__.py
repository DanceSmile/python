'''

在Python中，一个.py文件就称之为一个模块
为了避免模块名冲突，Python又引入了按目录来组织模块的方法，称为包（Package）。
每一个包目录下面都会有一个__init__.py的文件，这个文件是必须存在的
'''



'''
在Python中，安装第三方模块，是通过包管理工具pip完成的。

安装常用模块
用pip一个一个安装费时费力，还需要考虑兼容性。我们推荐直接使用Anaconda
'''

import  sys
'''
默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，搜索路径存放在sys模块的path变量中：
'''
r = sys.path
print(r)

# 如果我们要添加自己的搜索目录，有两种方法：
# 一是直接修改sys.path，添加要搜索的目录：
sys.path.append('/Users/michael/my_py_scripts')