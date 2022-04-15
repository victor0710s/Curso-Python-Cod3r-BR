from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql_2 = """INSERT INTO Contatos (nome, tel) VALUES (%s, %s)"""
args = ('Victor da Silva', '98822-4430')
with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql_2, args)
        connection.commit()
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        print('1 Register included, ID: ', cursor.lastrowid)
