from bd import new_connection
from mysql.connector.errors import ProgrammingError

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute('DROP TABLE IF EXISTS Emails')
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
