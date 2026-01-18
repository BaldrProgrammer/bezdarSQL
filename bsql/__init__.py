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

                attrs = [i for i in dir(table) if not '__' in i]
                print(attrs)

    except Exception as _e:
        print('error', _e)
