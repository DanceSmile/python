'''
由于Python是动态语言
根据类创建的实例可以任意绑定属性。
'''

# 实例属性，　
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

# 类属性
# 定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到
class Student(object):
    name = 'Student'