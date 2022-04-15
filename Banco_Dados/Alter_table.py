from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql = """ALTER TABLE Contatos ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY"""

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(sql)
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
