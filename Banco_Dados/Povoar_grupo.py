from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql_2 = 'INSERT INTO grupos (descricao) VALUES (%s)'
args = (
    ('Casa',),
    ('Trabalho',)
)


with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.executemany(sql_2, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        print(f'{cursor.rowcount} registers includeds!')
