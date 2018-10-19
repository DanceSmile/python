'''
获取对象信息
'''

class Animal(object):
    pass


# 基本类型都可以用type()判断：
r = type(Animal())
# <class '__main__.Animal'>
r = type(123)
# <class 'int'>
r = type(None)
# <class 'NoneType'>
# <class 'builtin_function_or_method'>
r = type(abs)

# 类型判断比较
'''
type(123) == int
Out[4]: True

type('abc') == type('123')
Out[5]: True

type('abc')==str
Out[6]: True

type('abc')==type(123)
Out[7]: False

'''

# 判断是否是列表里面的某一种类型
isinstance([1, 2, 3], (list, tuple))

# 获得一个对象的所有属性和方法
r = dir(Animal())
'''
类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度
'''
print(r)

