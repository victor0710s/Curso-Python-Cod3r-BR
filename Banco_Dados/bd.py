from mysql.connector import connect
from contextlib import contextmanager


parametros = dict(
    host='localhost',
    port=3306,
    user='root',
    password='vic321Tor',
    database='Agenda',
    auth_plugin='mysql_native_password'
)


@contextmanager
def new_connection():
    connection = connect(**parametros)
    try:
        yield connection
    finally:
        if (connection and connection.is_connected()):
            connection.close()
