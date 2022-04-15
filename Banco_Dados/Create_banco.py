from multiprocessing.dummy import connection
from mysql.connector import connect

conexao = connect(
    host='localhost',
    port=3306,
    user='root',
    password='vic321Tor',
    auth_plugin='mysql_native_password'
)

cursor = conexao.cursor()
cursor.execute('CREATE DATABASE Agenda')
