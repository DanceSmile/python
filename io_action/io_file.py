'''
io文件读写
'''

# 在磁盘上读写文件的功能都是由操作系统提供的
# 现代操作系统不允许普通的程序直接操作磁盘
# 所以，读写文件就是请求操作系统打开一个文件对象（通常称为文件描述符）

# 标示符'r'表示读，这样，我们就成功地打开了一个文件。
f = open('__init__.py',"r")

# 接下来，调用read()方法可以一次读取文件的全部内容
r = f.read()

# 关闭文件
f.close()


# 由于文件读写时都有可能产生IOError，一旦出错，后面的f.close()就不会调用。
# 所以，为了保证无论是否出错都能正确地关闭文件
# 我们可以使用try ... finally来实现
try:
    f = open('__init__.py', "r")
    print(f.read())
finally:
    if f:
        f.close()

# 但是每次都这么写实在太繁琐
# Python引入了with语句来自动帮我们调用close()方法：
with open('__init__.py', "r") as f:
    print(f.read())


# 调用read()会一次性读取文件的全部内容, read(size)读取指定大小的内容
# 调用readline()可以每次读取一行内容
# 用readlines()一次读取所有内容并按行返回list
f = open('__init__.py', "r")

for line in f.readlines():
    print(line)

# 　默认读取文本文件，并且是UTF-8编码的文本文件。
# 要读取二进制文件，比如图片、视频等等，用'rb'模式打开文件即可：
f = open('__init__.py', "rb")
r = f.read()

# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError
# 简单的方式是直接忽略
f = open('__init__.py', 'r', encoding='utf-8', errors
='ignore')

print(r)

f = open('file','w')
f.write('file io')
f.close()

# 希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入
with open('file', 'a') as f:
    f.write('Hello, world!')

'''
我们写文件时，操作系统往往不会立刻把数据写入磁盘，
而是放到内存缓存起来，空闲的时候再慢慢写入。
只有调用close()方法时，操作系统才保证把没有写入的数据全部写入磁盘。
忘记调用close()的后果是数据可能只写了一部分到磁盘，剩下的丢失了。
所以，还是用with语句来得保险
'''
