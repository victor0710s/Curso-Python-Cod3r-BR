from bd import new_connection
from mysql.connector.errors import ProgrammingError

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute('SHOW TABLES')
        for i, tables in enumerate(cursor, start=1):
            print(f'Tabelas {i}: {tables[0]}')
    except ProgrammingError as e:
        print(f'Error: {e.msg}')
