

import asyncio, os, json, time

from  datetime import datetime

from aiohttp import web




def index():

	return web.Response(body='hello')


@asyncio.coroutine
def init(loop):
	pass


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
