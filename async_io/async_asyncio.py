'''
asyncio标准库直接对异步io支持
asyncio可以是实现单线程的io并发操作。
异步操作需要在coroutine中通过yield from完成
多个coroutine可以封装成一组Task然后并发执行。
'''

# import asyncio
#
# @asyncio.coroutine
# def hello():
#     print('hello world!')
#     r = yield from asyncio.sleep(5)
#     print(" hello again")
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(hello())
# loop.close()

'''
asyncio.coroutine 可以把一个generator标记为一个coroutine类型
然后，我们就把这个coroutine扔到EventLoop中执行

hello() 首先执行print("hello!")
然后，yield from语法可以让我们方便地调用另一个generator

由于asyncio.sleep()也是一个coroutine
所以线程不会等待asyncio.sleep()，而是直接中断并执行下一个消息循环
当asyncio.sleep()返回时，线程就可以从yield from拿到返回值(None)，然后继续执行下一行语句

把asyncio.sleep(1)看成是一个耗时1秒的IO操作
此时，主线程并未等待，而是去执行EventLoop中其他可以执行的coroutine了，因此可以实现并发执行
'''

# 对上面的demo用两个coroutine进行改造实验,封装两个协程
# import  threading
# import asyncio
# @asyncio.coroutine
# def hello():
#     print('hello world! (%s)' % threading.currentThread())
#     yield from asyncio.sleep(5)
#     print('hello again ! (%s)' % threading.currentThread())
#
# tasks = [hello(), hello()]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

'''
hello world! (<_MainThread(MainThread, started 140501838137152)>)
hello world! (<_MainThread(MainThread, started 140501838137152)>)
(sleep about 1s)
hello again ! (<_MainThread(MainThread, started 140501838137152)>)
hello again ! (<_MainThread(MainThread, started 140501838137152)>)

由打印的当前线程名称可以看出，两个coroutine是由同一个线程并发执行的。
如果把asyncio.sleep()换成真正的IO操作，则多个coroutine就可以由一个线程并发执行。
'''

# 我们用asyncio的异步网络连接来获取sina、sohu和163的网站首页：
import  asyncio

@asyncio.coroutine
def wget(host):
    print("wget %s... " % host)
    connect = asyncio.open_connection(host,80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host,line.decode('utf-8').rstrip()))
    writer.close()

tasks = [wget(host) for host in ['www.sina.com.cn','www.163.com', 'www.163.com']]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

'''
wget www.163.com... 
wget www.sina.com.cn... 
wget www.163.com... 
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
www.163.com header > Date: Tue, 16 Oct 2018 02:28:07 GMT
www.163.com header > Content-Length: 0
www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header > Connection: close
www.163.com header > HTTP/1.0 302 Moved Temporarily
www.163.com header > Server: Cdn Cache Server V2.0
www.163.com header > Date: Tue, 16 Oct 2018 02:28:07 GMT
www.163.com header > Content-Length: 0
www.163.com header > Location: http://www.163.com/special/0077jt/error_isp.html
www.163.com header > Connection: close
www.sina.com.cn header > HTTP/1.1 302 Moved Temporarily
www.sina.com.cn header > Server: nginx
www.sina.com.cn header > Date: Tue, 16 Oct 2018 02:28:07 GMT
www.sina.com.cn header > Content-Type: text/html
www.sina.com.cn header > Content-Length: 154
www.sina.com.cn header > Connection: close
www.sina.com.cn header > Location: https://www.sina.com.cn/
www.sina.com.cn header > X-Via-CDN: f=edge,s=ctc.yongfeng.ha2ts4.182.nb.sinaedge.com,c=36.102.228.102;
www.sina.com.cn header > X-Via-Edge: 153965688790866e4662425721eda49424d02

'''