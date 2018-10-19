'''
类和实例
面向对象最重要的概念就是类（Class）和实例（Instance）
类是抽象的模板
实例是是一个具体的对象
'''

# 定义类
class Student(object):
    pass

# 创建类
bar = Student()

# __init 　初始化类　绑定属性
# 类的方法
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))

# 访问限制
# 禁止外部访问，可以把属性的名称前加上两个下划线__
class Student(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

# 内部访问
foo = Student('zero', 90)
foo.print_score()
zero: 90

# 外部访问
print(foo.__name)
# AttributeError: 'Student' object has no attribute 'name'



