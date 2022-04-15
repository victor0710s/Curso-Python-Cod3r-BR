from collections import defaultdict
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
        try:
            cursor.execute(sql)
            contatos = cursor.fetchall()
        finally:
            cursor.close()
    except ProgrammingError as e:
        print(f'ERRO : {e.msg}')
    else:
        agrupados = defaultdict(list)
        for contato in contatos:
            agrupados[contato['grupo']].append(contato['nome'])

        print(agrupados)


# 1 > Sera retornado como dicionario ficando assim mais facil de pegar as colunas pelo nome
