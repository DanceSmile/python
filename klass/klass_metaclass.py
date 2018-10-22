'''
元类
'''

class ModelMetaClass(type):
    def __new__(cls, name, bases, attrs):
        if name == 'Model':
            return type.__new__(cls, name, bases, attrs )
        else:
            mappings = dict()
            for  key, item  in attrs.items():
                if isinstance(item, Field):
                    mappings[key] = item
            for k in mappings.keys():
                attrs.pop(k)
            attrs['__mappings__'] = mappings
            if '__table__' not in  attrs:
                attrs['__table__'] = name
            return type.__new__(cls, name, bases, attrs )

class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kw):
        super().__init__(**kw)
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r' model not has attribute {}'.format(key))
    def __setattr__(self, key, value):
         self[key] = value
    def save(self):
        fields = []
        params = []
        for key, item in self.__mappings__.items():
            if key in self:
                params.append(self[key])
                fields.append(item.name)
        sql =  r'insert into {0} ({1}) values({2})'.format(self.__table__, ','.join(fields),  ','.join( map(str,params) ) )
        print(sql)

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return r'{}:{}'.format(self.__class__.__name__,self.name)


class InterField(Field):
    def __init__(self, name):
        super(InterField, self).__init__(name, 'int')

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class UserModel(Model):
    __table__ = "user"
    id = InterField('id')
    name = StringField('username')

class NewsModel(Model):
    __table__ = "news"
    id = InterField('id')
    content = StringField('content')

user = UserModel(name='zero', id=13)

user.save()

n = NewsModel(content='content')

n.save()



