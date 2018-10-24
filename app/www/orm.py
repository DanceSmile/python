import aiomysql, logging
logging.basicConfig(level=logging.INFO)

def log(sql, args=()):
    '记录操作sql日志'
    logging.info('SQL: {}'.format(sql))


def create_args_string(num):
    '''
    按照参数个数制作占位符号， 用于生成SQL语句
    #SQL的占位符是？，num是多少就插入多少个占位符
    '''
    L = ['?' for n in range(num)]
    return ', '.join(L)  # 将L拼接成字符串返回，例如num=3时："?, ?, ?"


async def create_pool(loop, **kw):
    ' 创建全局连接池，**kw 关键字参数集，用于传递host port user password db等的数据库连接参数 '
    logging.info('create database connection pool')
    global __pool  # 将__pool定义为全局变量
    __pool = await aiomysql.create_pool(
        host=kw.get('host', 'localhost'),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        port=3306,
        charset='utf8',
        loop=loop,
        autocommit=True
    )

async def destory_pool():
    global __pool
    # if __pool is not None:
    #     __pool.close()
    #     await __pool.wait_closed()

async def select(sql, args, size=None):
    ' 实现SQL语句：SELECT。传入参数分别为SQL语句、SQL语句中占位符对应的参数集、返回记录行数 '
    global __pool
    async with __pool.acquire()  as conn:
        async with conn.cursor(aiomysql.DictCursor) as cursor:
            await cursor.execute(sql.replace('?', '%s'), args or ())
            if size:
                res = await cursor.fetchmany(size)
            else:
                res = await cursor.fetchall()
        return res


async def execute(sql, args, autocommit=True):
    logging.info(sql)
    logging.info(args)
    global __pool
    async with (__pool.acquire()) as conn:
        if not autocommit:
            await conn.begin()
        try:
            async with  conn.cursor(aiomysql.DictCursor) as cursor:
                await cursor.execute(sql.replace("?", '%s'), args or ())
                affects = cursor.rowcount
            if not autocommit:
                await conn.commit()
        except BaseException as e:
            if not autocommit:
                await conn.rollback()
    return affects


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs)
        tableName = attrs.get("__table__", None) or name
        mappings = dict()
        fields = []
        primary_key = None
        for key, value in attrs.items():
            if isinstance(value, Field):
                mappings[key] = value
                if value.primary_key:
                    if primary_key:
                        raise ValueError('Duplicate primary key for field: %s' % k)
                    primary_key = key
                else:
                    fields.append(key)
        if not primary_key:
            raise ValueError('Primary key not found.')
        for k in mappings.keys():
            attrs.pop(k)
        escaped_fields = list(map(lambda f: '`%s`' % f, fields))
        attrs['__mappings__'] = mappings
        attrs['__table__'] = tableName.lower()
        attrs['__primary__'] = primary_key
        attrs['__fields__'] = fields
        attrs['__select__'] = 'select `%s` , %s  from  `%s` ' % (primary_key, ','.join(escaped_fields), tableName)
        attrs['__insert__'] = 'insert into `%s` (%s, `%s`) values (%s) ' % (tableName, ','.join(escaped_fields), primary_key,create_args_string(len(fields)+1))
        attrs['__update__'] = 'update  %s  set %s where `%s` = ? ' % (tableName, ','.join(map(lambda f:  '%s = ?' % f ,escaped_fields)), primary_key )
        attrs['__delete__'] = 'delete from `%s` where `%s`=?' % (tableName, primary_key)
        return type.__new__(cls, name, bases, attrs)


class Model(dict, metaclass=ModelMetaclass):
    def __init__(self, **kw):
        super(Model, self).__init__(**kw)
    def __getattr__(self, item):
        try:
            return self[item]
        except KeyError:
            raise AttributeError

    def __setattr__(self, key, value):
        self[key] = value

    def getValue(self, key):
        return getattr(self, key, None)

    def getValueOrDefault(self, key):
        value = self.getValue(key)
        if value is None:
            field = self.__mappings__[key]
            if field.default is not None:
                value = field.default() if callable(field.default) else field.default
                setattr(self, key, value)
        return value

    @classmethod
    async def findAll(cls, where=None, args=None, **kw):
        sql = [cls.__select__]
        if where:
            sql.append('where')
            sql.append(where)
        if args is None:
            args = []
        orderBy = kw.get('orderBy', None)
        if orderBy:
            sql.append('orderBy')
            sql.append(orderBy)
        limit = kw.get('limit', None)
        if limit:
            sql.append('limit')
            if isinstance(limit, int):
                sql.append('?')
                args.append(limit)
            elif isinstance(limit, tuple) and len(limit) == 2:
                sql.append('?, ?')
                args.extend(limit)
            else:
                raise ValueError('type is nor support')
        rs = await select(','.join(sql), args)
        return rs

    @classmethod
    async def find(cls, pk):
        logging.info('%s where `%s` = ?' % (cls.__select__, cls.__primary__))
        logging.info(pk)
        rs = await select('%s where `%s` = ?' % (cls.__select__, cls.__primary__), (pk,))
        await destory_pool()
        if len(rs) == 0:
            return None
        return cls(**rs[0])

    async def save(self):
        args = list(map(self.getValueOrDefault, self.__class__.__fields__))
        args.append(self.getValueOrDefault(self.__class__.__primary__))
        logging.info(self.__class__.__insert__)
        logging.info(args)
        rows = await execute(self.__class__.__insert__,args)
        await destory_pool()
        if rows != 1:
            logging.warn('fail to insert ')
        return rows
    async def update(self):
        '''
        update  table set
        :return:
        '''
        args = list(map(self.getValueOrDefault, self.__class__.__fields__))
        args.append(self.getValue(self.__primary__))
        rows = await execute(self.__update__, args)
        if rows != 1:
            logging.warn('failed to update by primary key : affected rows: %s' % rows)

    async def remove(self):
        ' 实例方法，映射根据主键值删除记录 '
        args = [self.getValue(self.__primary__)]
        rows = await execute(self.__delete__, args)
        if rows != 1:
            logging.warn('failed to remove by primary key: affected rows: %s' % rows)

class Field(object):
    def __init__(self, name, column_type, primary_key, default):
        self.name = name
        self.column_type = column_type
        self.default = default
        self.primary_key = primary_key

    def __str__(self):
        return '<%s, %s:%s>' % (self.__class__.__name__, self.column_type, self.name)


class StringField(Field):
    def __init__(self, name=None, default=None, primary_key=False, ddl='varchar(100)'):
        super(StringField, self).__init__(name, ddl, primary_key, default)


class BooleanField(Field):
    ' 从Field继承，定义一个布尔类，在ORM中对应数据库的布尔类型 '

    def __init__(self, name=None, default=0):
        ' 可传入参数列名、默认值 '
        super().__init__(name, 'boolean', False, default)  # 对应列名、数据类型、主键、默认值


class IntegerField(Field):
    ' 从Field继承，定义一个整数类，在ORM中对应数据库的 BIGINT 整数类型，默认值为0 '

    def __init__(self, name=None, primary_key=False, default=0):
        ' 可传入参数列名、主键、默认值 '
        super().__init__(name, 'bigint', primary_key, default)


class FloatField(Field):
    ' 从Field继承，定义一个浮点数类，在ORM中对应数据库的 REAL 双精度浮点数类型 '

    def __init__(self, name=None, primary_key=False, default=0.0):
        super().__init__(name, 'real', primary_key, default)


class TextField(Field):
    ' 从Field继承，定义一个文本类，在ORM中对应数据库的 TEXT 长文本数类型 '

    def __init__(self, name=None, default=None):
        super().__init__(name, 'text', False, default)
