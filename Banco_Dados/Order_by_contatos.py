from bd import new_connection

sql = "SELECT nome, id FROM Contatos ORDER BY nome DESC"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print('\n'.join(str(registro) for registro in cursor))
