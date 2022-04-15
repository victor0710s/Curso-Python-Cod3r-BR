from bd import new_connection

sql = "SELECT * FROM Contatos WHERE tel = '98847-1998'"

with new_connection() as connection:
    cursor = connection.cursor()
    cursor.execute(sql)

    for x in cursor:
        print(x)
