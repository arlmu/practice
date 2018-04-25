
#metaclass 是类的模板，所以必须从'type'类型派生：
class ListMetaclass(type):
    def __new__ (cls, name, bases, attrs):
        attrs['add'] = lambda self, value: self.append(value)
        return type.__new__(cls, name, bases, attrs)

class MyList(List, metaclass=ListMetaclass):
    pass

L=MyList()
L.add(1)



#ORM
class User(Model):
    #定义类的属性到列的映射
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


#创建一个实例：
u = User(id=12345, name='Micheal', emil='test@orm.org',password='my-pwd')
#保存到数据库：
u.save()

#首先定义Field类,它负责保存数据库的字段名和字段类型：
class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.colmu_type = column_type

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)


class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')


class ModelMetaclass(type):
    def __new__(cls, name, bases, attrs):
        return=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Fount model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping:%s ==> %s' % (k,v))
                mappings[k] = v
            for k in mappings.key():
                attrs.pop(k)
            attrs['__mappings__'] = mappings
            attrs['__table__'] = name
            return type.__new__(cls, name, bases, attrs)



