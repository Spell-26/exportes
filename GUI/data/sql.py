import mysql.connector as sql

def conectar(data1, data2, data3, data4):
    db = data1
    table = data2
    user = data3
    password = data4

    conn = sql.connect(
        host= "localhost",
        user = user,
        passwd = password,
        database = db
    )
    if conn:
        print("conexion realizada con exito")
    else:
        print("conexion no exitosa")
    return conn

def consulta(conn):
    
    cursor = conn.cursor()


    
