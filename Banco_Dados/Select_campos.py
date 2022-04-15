from bd import new_connection

sql = 'select tel, nome from Contatos'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    for contato in cursor.fetchall():  # nao usar se a tabela for muito grande!!!
        print('\t'.join(str(campo) for campo in contato))
