
import logging;
logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time

from  datetime import datetime

from aiohttp import web


def index(request):
	return web.Response(body='hello world')


async def init(loop):
	app = web.Application(loop=loop)
	app.router.add_route('GET', "/", index)
	server = await loop.create_server(app.make_handler(), '', 9000)
	logging.info('server start at http://127.0.0.1:9000')
	return server



loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()







