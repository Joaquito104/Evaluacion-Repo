import mysql.connector
from mysql.connector import Error

def obtener_conexion():
    try:
        # Establecer conexión con la base de datos
        conexion = mysql.connector.connect(
            host="localhost",    
            user="root",          
            password="password",                #Cambiarlos una vez creada la conexion manual al dispositivo del cliente
            database="database"    
        )
        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
            return conexion
    except Error as e:
        print("Sacate la zapatilla:", e)
        return None

def cerrar_conexion(conexion):
    if conexion and conexion.is_connected():
        conexion.close()
        print("Fuiste Bueno")
