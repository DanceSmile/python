'''
基础语法
'''


'''
Python内置的一种数据类型是列表：list
list是一种有序的集合，可以随时添加和删除其中的元素。

'''
# 声明一个list
r = [ 1,2,3,5,6,7,8,'zero']

# 索引访问
print(r[3])
print(r[5])

# 负数索引访问
r[-1]
r[-3]

# 列表长度
len(r)

# 在列表尾部住家元素
r.append('append')

# 在任意位置插入元素
r.insert(0,'first')
# 替换指定位置的元素
r[0] = 'stead'
# 删除末尾元素
r.pop()
# 删除指定位置的元素
r.pop(1)


# 切片
# 复制一个list
r = r[:]
# 0-8
r[0:8]



print(r)

'''
元组
tuple和list非常类似，但是tuple一旦初始化就不能修改
'''

# 声明元组
t = ('Bob', "Alice")
# 声明空元组
t = ()
# 声明一个元素的元组
t = (1, )



'''
dict字典
'''

# 声明一个字典
d = { "name": 'zero', "age":19}



# 获取元素
r = d['name']
# 获取元素带默认值
r = d.get('name', 'default')
# 添加元素
d['result'] = "single"
print(r)

# 判断元素是否存在
r = 'name' in d
# True
print(r)

# 删除元素
d.pop('name')
# {'age': 19, 'result': 'single'}
print(d)



'''
条件判断
'''

age = 20

if age >= 6:
    print('teenager')
elif age >= 18:
    print('adult')
else:
    print('kid')



'''
循环
'''

# 1+2+3+4+5......+100
sum = 0
for x in range(101):
    sum = sum+x
print(sum)

sum1 = 0
n = 100
while n>0:
    sum1 = sum1+n
    n = n-1
print(sum1)

l = [1,2,3,4,5,6,7]

for i, value in enumerate(l):
    print(value)
'''
set 集合
set和dict类似，也是一组key的集合，但不存储value。
由于key不能重复，所以，在set中，没有重复的key。
'''

# 声明一个集合
s = set([1,2,34])

print(s)

# 集合的元素不能重复，如果有则回过滤掉重复的元素
s = set([1,2,3,4,5,63,5,3])
print(s)

# 添加元素
s.add('zero')
print(s)

# 删除元素
s.remove(1)
print(s)



s1 = set([1,2,4,54,5,6,89])
s2 = set([54,89,7,56])

# 求两个集合的交集
print(s1 & s2)

# 求两个集合的并集
print(s1|s2)


# 列表生成器。
l = [1,2,4,5,6,67,7]
r =  [ value*2 for value in l if value%2 ==0 ]

print(r)

# 生成器
l = [1,2,4,5,6,67,7]
r =  (value*2 for value in l if value%2 ==0 )
print(r)

# 迭代器

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator

from collections import Iterable

# 检测是否是可迭代对象

isinstance([], Iterable)
isinstance(( x for x in range(100)), Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。





