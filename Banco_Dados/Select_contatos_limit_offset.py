from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql = 'select * from Contatos LIMIT 4 OFFSET 2'

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
        contatos = cursor.fetchall()  # nao usar se a tabela for muito grande!!!
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato[2]:2d} - {contato[0]:16s} Telefone: {contato[1]}')
