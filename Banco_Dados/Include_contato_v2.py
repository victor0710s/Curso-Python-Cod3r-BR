from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql_2 = """INSERT INTO Contatos (nome, tel) VALUES (%s, %s)"""
args = (
    ('Zuclene M', '98847-1998'),
    ('Uales Santos', '97337-7522'),
    ('Bom dia CIA', '4002-8922'),
    ('Gustavo Lima', '99912-5003'),
    ('Valenet', '3563-9900')
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
