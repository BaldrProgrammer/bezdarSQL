# from config import *
# import psycopg2
#
# try:
#     with psycopg2.connect(
#             host=host,
#             port=port,
#             user=user,
#             database=db_name,
#             password=password,
#     ) as connection:
#         connection.autocommit = True
#         with connection.cursor() as cursor:
#             cursor.execute("""
#                 select * from ads;
#             """)
#
#             print(cursor.fetchall())
#
# except Exception as _e:
#     print('error', _e)
def select(tablename, **kwargs):
    request = f'select {kwargs['value']} from {tablename} where '
    filters = kwargs['filter_by']
    for fil in filters:
        request += f'and {fil}={filters[fil]}'
    return request + ';'

print(select('ads', value='*', filter_by={'id': '1'}))