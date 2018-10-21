
import aiomysql

async def create_pool(loop, **kw):
	global __loop

	__pool = await aiomysql.create_pool(
		host =  'localhost',
		user = 'root',
		password = 'root',
		database = 'gpi',
		port = 3306,
		charset='utf8',
		loop=loop,
		autocommit=True
	)



