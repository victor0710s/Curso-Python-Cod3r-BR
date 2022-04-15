from mysql.connector import ProgrammingError
from bd import new_connection

table_contatos = """
    CREATE TABLE IF NOT EXISTS Contatos(nome VARCHAR(50), tel VARCHAR(40))
"""

table_emails = """
    CREATE TABLE Emails(
        id INT AUTO_INCREMENT PRIMARY KEY, 
        dono VARCHAR(50)
    )
"""

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_contatos)
            cursor.execute(table_emails)
        except ProgrammingError as e:
            print(f'ERRO : {e.msg}')
except ProgrammingError as e:
    print(f'ERRO Connection: {e.msg}')
