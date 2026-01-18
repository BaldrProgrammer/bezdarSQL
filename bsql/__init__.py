from .config import *
import psycopg2

def select(table, **kwargs):
    request = f'select {kwargs['value']} from {table.__tablename__} where '
    filters = kwargs['filter_by']
    index = 0
    for fil in filters:
        index += 1
        if index > 1:
            request += f'and {fil}={filters[fil]} '
        else:
            request += f'{fil}={filters[fil]} '

    try:
        with psycopg2.connect(
                host=host,
                port=port,
                user=user,
                database=db_name,
                password=password,
        ) as connection:
            connection.autocommit = True
            with connection.cursor() as cursor:
                cursor.execute(request + ';')
                result = cursor.fetchone()

                attrsintable = [i for i in table.__dict__ if not '__' in i]
                attrs = {}
                for index, attr in enumerate(attrsintable):
                    attrs[attr] = result[index]
                obj = table()
                obj.__dict__.update(attrs)

                return obj

    except Exception as _e:
        print('error', _e)


def insert(obj):
    request = f'insert into {obj.__tablename__} ('
    attrs = [i for i in obj.__dict__ if '__' not in i]
    for index, attr in enumerate(attrs):
        value = getattr(obj, attr)
        if hasattr(value, 'autoincrement'):
            if not value.autoincrement:
                request += f'{attr}' + (', ' if not index+1 == len(attrs) else '')
        else:
            request += f'{attr}' + (', ' if not index+1 == len(attrs) else '')

    request += ') values ('
    for index, attr in enumerate(attrs):
        value = getattr(obj, attr)
        if hasattr(value, 'autoincrement'):
            if not value.autoincrement:
                request += repr(value) + (', ' if not index+1 == len(attrs) else ');')
        else:
           request += repr(value) + (', ' if not index+1 == len(attrs) else ');')
    print(request)
