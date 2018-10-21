'''
装饰器
'''

# 打印当前时间
def now():
    print('2018-10-10')

f = now
f()


# 装饰器函数
def log(fun):
    print("log")
    def warp(*arg, **kw):
        return fun(*arg, **kw)
    return warp

log(now)()


# python @使用装饰器。

@log
def now():
    print('@ use decorator')

now()


# 装饰器本身就有参数


def log(text):
    def decorator(fun):
        def warp(*arg, **kw):
            print(text)
            return fun(*arg, **kw)
        return warp
    return decorator


log('cailei')(now)()


