from bd import new_connection

sql = "SELECT * FROM Contatos WHERE nome like %s"

with new_connection() as connection:
    nome = input('Contato a ser localizado: ')
    args = (f'%{nome}%', )

    cursor = connection.cursor()
    cursor.execute(sql, args)

    for x in cursor:
        print(x)
