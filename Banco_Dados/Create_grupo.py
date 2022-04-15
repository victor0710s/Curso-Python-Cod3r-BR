from mysql.connector import ProgrammingError
from bd import new_connection

table_grupo = """
    CREATE TABLE IF NOT EXISTS grupos(
        id INT AUTO_INCREMENT PRIMARY KEY,
        descricao VARCHAR(30)
    )
"""
alter_table_contatos_1 = """
    ALTER TABLE Contatos ADD group_id INT
"""

alter_table_contatos_2 = """
    ALTER TABLE Contatos ADD FOREING KEY (group_id),
    REFERENCES grupos (id)
"""

try:
    with new_connection() as connection:
        try:
            cursor = connection.cursor()
            cursor.execute(table_grupo)
            cursor.execute(alter_table_contatos_1)
            cursor.execute(alter_table_contatos_2)
        except ProgrammingError as e:
            print(f'ERRO : {e.msg}')
except ProgrammingError as e:
    print(f'ERRO Connection: {e.msg}')
