from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql = "UPDATE Contatos SET tel = %s WHERE id like %s"
args = ('95847-1352', 6)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        print(f'{cursor.rowcount} register(s) updated.')
