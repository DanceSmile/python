'''
面向对象基础
'''

# 面向过程　vs 面向对象
std1 = {'name': "Bob", 'age': 19}
std2 = {'name': "Alice", 'age': 17}
def print_age(std):
    print('%s age is %s' % (std['name'], std['age']))

print_age(std1)
print_age(std2)

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def print_age(self):
        print('%s age is %s' % (self.name, self.age))

std1 = Student('Bob', 19)
std2 = Student('Alice', 17)
std1.print_age()
std2.print_age()

'''
面向对象的设计思想是从自然界中来的
因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，
而实例（Instance）则是一个个具体的Student，
比如，Bart Simpson和Lisa Simpson是两个具体的Student。

所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。

面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。
'''


