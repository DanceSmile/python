'''
动态添加属性和方法
'''

class Student(object):
    pass

s = Student()
# 动态添加实例属性
s.name = "zero"

def set_age(self):
    self.age = 10

from types import MethodType

# 动态添加实例方法
s.set_age = MethodType(set_age, s)
s.set_age()

# 动态给class添加方法
Student.set_age = set_age

print(s.age)
#
# 为了达到限制的目的，Python允许在定义class的时候，
# 定义一个特殊的__slots__变量，来限制该class实例能添加的属性
class Student(object):
    __slots__ = ('name', 'age', 'set_age') # 用tuple定义允许绑定的属性名称


s = Student()
s.set_age = MethodType(set_age, s)
s.age_ = 123
