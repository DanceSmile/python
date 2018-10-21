'''
函数闭包
'''


def sum(*num):
    r = 0
    for item in num:
        r+=item
    return r

print(sum(1,2,4,4,5))

def sum(*num):
    def lazy_sum():
        r = 0
        for item in num:
            r += item
        return r

    return lazy_sum


r = sum(1,2,34,5,5)

print(r())

