from bd import new_connection
from mysql.connector.errors import ProgrammingError

sql = """
    SELECT
        grupos.descricao AS grupo,
        contatos.nome AS nome
    FROM contatos
    INNER JOIN grupos ON contatos.group_id = grupos.id
    ORDER BY grupo, nome
"""

with new_connection() as connection:
    try:
        cursor = connection.cursor(dictionary=True)  # 1
        cursor.execute(sql)
        contatos = cursor.fetchall()
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        for contato in contatos:
            print(f'{contato["grupo"]}: {contato["nome"]}')


# 1 > Sera retornado como dicionario ficando assim mais facil de pegar as colunas pelo nome
