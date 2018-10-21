'''
偏函数
'''

# 使用偏函数创建新的函数 固定默认值


from functools import partial

int2 = partial(int, base=2)

r = int2('1')
print(r)

# 可变参数*args的一部分自动加到左边
max2 = partial(max,10)
r = max2(1,2,4)
# 相当于 max(10, 1, 2,4)

print(r)

