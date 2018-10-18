'''
Python从3.5版本开始为asyncio提供了async和await的新语法

用asyncio提供的@asyncio.coroutine可以把一个generator标记为coroutine类型
然后在coroutine内部用yield from调用另一个coroutine实现异步操作

为了简化并更好地标识异步IO，从Python 3.5开始引入了新的语法async和await，可以让coroutine的代码更简洁易读。

请注意，async和await是针对coroutine的新语法，要使用新的语法，只需要做两步简单的替换：
1. 把@asyncio.coroutine替换为async；
2. 把yield from替换为await。
注意新语法只能用在Python 3.5以及后续版本
之前版本则仍需使用asyncio案例的方案。

'''

import asyncio

# 之前代码
@asyncio.coroutine
def hello1():
    print('hello world!!')
    yield from asyncio.sleep(3)
    print('hello again!')

# 新代码更加简洁
async  def hello():
    print('hello world!!')
    await asyncio.sleep(3)
    print('hello again!')

tasks = [hello1(),hello()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
结果任然一致，不受影响
hello world!!
hello world!!
hello again!
hello again!
'''