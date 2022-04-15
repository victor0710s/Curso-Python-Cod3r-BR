from bd import new_connection

sql = 'select tel, nome from Contatos LIMIT 4 OFFSET 3'

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
    print(cursor.fetchone())
