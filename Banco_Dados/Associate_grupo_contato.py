from bd import new_connection
from mysql.connector.errors import ProgrammingError

select_group = 'SELECT id FROM grupos WHERE descricao = %s'
update_contato = 'UPDATE Contatos SET group_id = %s WHERE nome = %s'

contato_grupo = {
    'Zuclene M': 'Trabalho',
    'Uales Santos': 'Casa',
    'Bom dia CIA': 'Trabalho',
    'Gustavo Lima': 'Trabalho',
    'Valenet': 'Casa',
}

with new_connection() as connection:
    try:
        cursor = connection.cursor()
        for contato, grupo in contato_grupo.items():
            cursor.execute(select_group, (grupo,))
            grupo_id = cursor.fetchone()[0]
            cursor.execute(update_contato, (grupo_id, contato))
            connection.commit()
    except ProgrammingError as e:
        print(f'ERRP : {e.msg}')
    else:
        print('Contatos Associados')
