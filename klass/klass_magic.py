'''
class 定制类
'''

class Test(object):

    a = 1

    # 已经定义的属性的装饰输出
    def __getattribute__(self, item):
        pass



    # print输出
    def __str__(self):

        return "__str__"

    # 返回一个可以迭代的对象
    def __iter__(self):
        return self

    # 使用for循环
    def __next__(self):
        Test.a+=1
        if Test.a > 100:
            raise StopIteration
        return Test.a

    # 使用键名
    def __getitem__(self, item):

        if item == 'test':
            return "get item test"

    # 获取未定义的属性
    def __getattr__(self, item):

        return "None"

    # 直接使用实例函数
    def __call__(self, *args, **kwargs):
        print("__call__")





t = Test()


print(t)

for x in Test():
    print(x)


print(t['test'])

print(t.zero)

t()