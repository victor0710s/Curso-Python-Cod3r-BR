from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql = "DELETE FROM Contatos WHERE nome = %s"
args = ('Victor da Silva',)

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        print(f'{cursor.rowcount} register(s) deleted.')
