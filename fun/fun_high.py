'''
function高级特性
'''


# map/reduce

L = [1,2,3,45,6,6]

# 自定义处理函数
def  f(x):
    return x*x

r = list(map(f, L))
# [1, 4, 9, 2025, 36, 36]

print(r)


# 利用内置的处理个函数
r = list(map(str, L))
print('=================')
print(r)


from functools import  reduce

# 利用reduce计算总和
r = reduce(lambda x,y:x+y, L)
print(r)


# filter 过滤函数

L = [1,2,4,5,6,7,78,8,9,10]

r = list(filter(lambda x : (x%2), L))

print(r)

# sored 排序

r = sorted([12,46,23,6,78,8,89], key=lambda x: x)
print(r)
