import orm, asyncio
from models import User, Blog, Comment




async def test_orm(loop):
    await orm.create_pool(loop,user='root',password='root',db='awesome')
    # u = User(name='Test10', email='te13st123111233442@example.com', passwd='123456', image='about:blank')
    # await u.save()

    # u = User(name='12',image='about:blank',id='001540279748738d7912142c0f44cb397fe74d66a876010000')
    # await u.update()


    c = User()
    user = await c.find('001540279835405b2cc350d72314331b367880643f0ea91000')
    await user.remove()
    print(await user.findAll())




loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait([test_orm(loop)]))
loop.run_forever()

