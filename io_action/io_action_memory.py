'''
stringIo
在内存中操作str

bytesIO
在内存中操作字节
'''

from  io import StringIO

# 创建stringIo对象
f = StringIO()

# 写入str数据
f.write('hello \n')
f.write('world')

# 读取
r = f.getvalue()

# 初始化stringIO 可以和文件 一样读取
f = StringIO('hello \r world\r !!')


# 读取
r = f.readline()
f.read()
f.readlines()
print(r)


'''
bytesIO
    
'''
from io import BytesIO
f = BytesIO()

# 写入读取文件
f.write('cailei'.encode('utf-8'))
# tell 方法获取当前文件读取指针的位置
# seek 方法，用于移动文件读写指针到指定位置,有两个参数，第一个offset: 偏移量，需要向前或向后的字节数，正为向后，负为向前；
# 第二个whence: 可选值，默认为0，表示文件开头，1表示相对于当前的位置，2表示文件末尾
# 用seek方法时，需注意，如果你打开的文件没有用'b'的方式打开，则offset无法使用负值哦

f.seek(0,0)
print(f.tell())
print(f.read())

r = f.getvalue()


# 初始化字节内存

f = BytesIO(b'cailei')



