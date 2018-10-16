'''
asyncio可以实现单线程并发IO操作

如果仅用在客户端，发挥的威力不大。
如果把asyncio用在服务器端，由于HTTP连接就是IO操作，因此可以用单线程+coroutine实现多用户的高并发支持。

asyncio实现了TCP、UDP、SSL等协议，
aiohttp则是基于asyncio实现的HTTP框架

'''

from  aiohttp import  web
import asyncio

async def index(request):
    return web.Response(body = b'hello index', content_type='text/html')

async def hello(request):
    text = 'hello {}'.format(request.match_info['name'])
    return web.Response(body=text.encode('utf-8'), content_type='text/html')

async def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route("GET", '/hello/{name}', hello)
    server = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print("server is running ")
    return server

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

'''
aiohttp的初始化函数init()也是一个coroutine
loop.create_server()则利用asyncio创建TCP服务。

http://127.0.0.1:8000/hello/foo
hello foo

http://127.0.0.1:8000/
hello index
'''


