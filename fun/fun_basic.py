'''
function basic
'''


'''
定一个函数
'''
def my_abs(x):
    return abs(x)

# 调用函数
r = my_abs(-10)



'''函数参数'''


# 位置参数

def my_func(x, y):

    return x,y

r = my_func(1,2)

# 默认参数 y参数缺省值为5
# 一是必选参数在前，默认参数在后，否则Python的解释器会报错
def my_func(x, y = 5):
    return x, y

r = my_func(5)

def my_register(name, sex='F', city='Beijing'):

    return name, sex, city

# 按照参数名称指定值， 可以不按照顺序传入参数
r = my_register( city='shanghai', name='zero')


# 默认参数尽量使用不可变对象
def add_end(L=[]):
    L.append('end')
    return L

r  = add_end([1,2,3])
r = add_end([7,4,3])

r = add_end()
r = add_end()


# 可变参数

def calc(*number):
    print( type(number) )
    result = 0
    for  x in number:
        result += x

    return result


r = calc(1,2,3,4,5)


# 关键词参数
def person(name, age, **kw):
    print("name:", name, 'age:', age, 'other', kw)


r = person('zero', 18, city='beijing', home='shuyang')

# 命名关键字参数
def person(name, age, *, city, job):
    print(name, age, city, job)

r = person('zero', 18,  city='beijin', job='program')
print(r)


'''
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
'''