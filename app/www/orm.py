import aiomysql


def create_args_string(num):
    '''
    按照参数个数制作占位符号， 用于生成SQL语句
    #SQL的占位符是？，num是多少就插入多少个占位符
    '''
    L = [ '?' for n in range(num)]
    return ', '.join(L) #将L拼接成字符串返回，例如num=3时："?, ?, ?"


print(create_args_string(3))



async def create_pool(loop, **kw):
    global __pool
    __pool = await aiomysql.create_pool(
        host='localhost',
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        port=3306,
        charset='utf8',
        loop=loop,
        autocommit=True
    )


async def select(sql, args, size=None):
    global __pool
    async with (__pool.acquire())  as conn:
        cursor = await conn.cursor(aiomysql.DictCursor)
        await cursor.execute(sql.replace('?', '%s'), args or ())
        if size:
            res = await cursor.fetchmany(size)
        else:
            res = await cursor.fetchall()
        await cursor.close()
        return res


async def execute(sql, args):
    global __pool
    async with (__pool.acquire()) as conn:
        async with  conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(sql.replace("?", '%s'), args or ())
            affects = cursor.rowcount
    return affects


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        tableName = attrs.get("__table__", None) or name
        mappings = dict()
        primary_key = 'id'
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        else:
            for key, value in attrs.items():
                if isinstance(value, Field):
                    mappings[key] = value
                    if value.primary:
                        primary_key = key
            for k in mappings.keys():
                attrs.pop(k)
            attrs['__mappings__'] = mappings
            attrs['__table__'] = tableName.lower()
            attrs['__primary__'] = primary_key
            attrs['__select__'] = r'select * from {0}'.format(tableName)
            return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)

    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise ValueError

    def __setattr__(self, key, value):
        self[key] = value

    @classmethod
    async def find(cls, id=None):
        if id:
            return await select('select * from {0} where {1} = ? '.format(cls.__table__, cls.__primary__), (id,))
        return await select('select * from {0}'.format(cls.__table__), ())

    async def update(self):
        if not self.__primary__:
            raise KeyError
        field = []
        for key, item in self.__mappings__.items():
            if key in self:
                field.append(key)

        sql = 'update  {0} ({1}) values({2}) where {3}={4}'.format(
            self.__table__,
            ','.join(map(str, field)),
            ','.join(list(map(lambda key: '%s', field)))
        )
        args = tuple(
            map(lambda key: (getattr(self, key)), field)
        )
        return await execute(sql, args)

    async def save(self):
        field = []
        for key, item in self.__mappings__.items():
            if key in self:
                field.append(key)

        sql = 'insert into {0} ({1}) values({2})'.format(
            self.__table__,
            ','.join(map(str, field)),
            ','.join(list(map(lambda key: '%s', field)))
        )
        args = tuple(
            map(lambda key: (getattr(self, key)), field)
        )
        return await execute(sql, args)


class Field(object):
    def __init__(self, name, column_type, default, primary=False):
        self.name = name
        self.column_type = column_type
        self.default = default
        self.primary = primary


class StringField(Field):
    def __init__(self, name, default=None, primary=False):
        super(StringField, self).__init__(name, 'varchar(100)', default, primary)


class InterField(Field):
    def __init__(self, name, default=None, primary=False):
        super(InterField, self).__init__(name, 'int', default, primary)
