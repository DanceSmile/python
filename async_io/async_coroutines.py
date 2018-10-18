'''
特点
子程序是层级调用执行顺序明确
协程类似于子程序，但是在执行过程中可以中断转而执行别的程序，在适当的时候再返回回来继续执行

优势
１.协程执行效率高，协程是在一个线程里执行，所以没有切换线程的开销
2.不需要多线程的锁机制，因为只有一个线程，也不存在同时写变量冲突，
在协程中控制共享资源不加锁，只需要判断状态就好了，所以执行效率比多线程高很多

python的协程是通过generator实现：
1.generator可以使用for循环来迭代，还可以使用next()调用来获取yield语句返回的下一个值
2.yield不但可以返回一个值，还以接受调用者发出的参数

例子：
生产消费模型
1. 调用c.send(None)启动生成器
2. 一旦生产了东西，通过c.send(n)切换到consumer执行
3. consumer通过yield拿到消息，处理，又通过yield把结果传回
4. produce拿到consumer处理的结果，继续生产下一条消息
5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束
整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

执行流程：
１.首先调用c.send(None)启动生成器
2.然后一旦产生了东西，就通过c.send(n)切换到consumer执行
3.consumer通过yield拿到消息，又通过yield把结果传回来
4.produce拿到consumer处理的结果，继续生产下一条消息
5.produce决定不生产了，通过c.close()关闭consumer，整个过程结束

执行结果
[producer] producing 1
[consumer] consuming 1
[producer] consumer return  200 ok
[producer] producing 2
[consumer] consuming 2
[producer] consumer return  200 ok
[producer] producing 3
[consumer] consuming 3
[producer] consumer return  200 ok
[producer] producing 4
[consumer] consuming 4
[producer] consumer return  200 ok
[producer] producing 5
[consumer] consuming 5
[producer] consumer return  200 ok

'''

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[consumer] consuming %s' % n)
        r = '200 ok'

def produce(c):
    c.send(None)
    n = 0
    while n<5:
        n = n+1
        print("[producer] producing %s" % n)
        r = c.send(n)
        print("[producer] consumer return  %s" % r)
    c.close()


c = consumer()
produce(c)