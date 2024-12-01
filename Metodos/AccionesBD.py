from ConexionBD import obtener_conexion, cerrar_conexion

# Función para agregar un registro
def agregar_registro(fecha_entrada, fecha_salida, estado):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = """
        INSERT INTO registros (fecha_entrada, fecha_salida, estado)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (fecha_entrada, fecha_salida, estado))
        conexion.commit()
        print("Registro agregado exitosamente.")
        cerrar_conexion(conexion)

# Función para eliminar un registro por ID
def eliminar_registro(id):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "DELETE FROM registros WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        print(f"Registro con ID {id} eliminado exitosamente.")
        cerrar_conexion(conexion)

# Función para buscar un registro por ID
def buscar_registro(id):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM registros WHERE id = %s"
        cursor.execute(query, (id,))
        registro = cursor.fetchone()
        if registro:
            print(f"Registro encontrado: ID {registro[0]}, Entrada: {registro[1]}, Salida: {registro[2]}, Estado: {registro[3]}")
        else:
            print(f"No se encontró un registro con ID {id}.")
        cerrar_conexion(conexion)

# Función para mostrar todos los registros
def mostrar_registros():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM registros"
        cursor.execute(query)
        registros = cursor.fetchall()
        if registros:
            for registro in registros:
                print(f"ID {registro[0]}, Entrada: {registro[1]}, Salida: {registro[2]}, Estado: {registro[3]}")
        else:
            print("No hay registros disponibles.")
        cerrar_conexion(conexion)

# Función para registrar un pago en un registro
def registrar_pago(monto, id):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "UPDATE registros SET estado = 'Pagado' WHERE id = %s"
        cursor.execute(query, (id,))
        conexion.commit()
        print(f"Pago de {monto} registrado exitosamente en el registro con ID {id}.")
        cerrar_conexion(conexion)

# Función para cambiar el estado de un registro
def cambiar_estado(id, nuevo_estado):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "UPDATE registros SET estado = %s WHERE id = %s"
        cursor.execute(query, (nuevo_estado, id))
        conexion.commit()
        print(f"Estado del registro con ID {id} cambiado a '{nuevo_estado}'.")
        cerrar_conexion(conexion)

# Función para agregar una habitación
def agregar_habitacion(numero, tipo):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO habitaciones (numero, tipo) VALUES (%s, %s)"
        cursor.execute(query, (numero, tipo))
        conexion.commit()
        print(f"Habitación {numero} agregada exitosamente.")
        cerrar_conexion(conexion)

# Función para ver todas las habitaciones
def ver_habitaciones():
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "SELECT * FROM habitaciones"
        cursor.execute(query)
        habitaciones = cursor.fetchall()
        if habitaciones:
            for habitacion in habitaciones:
                print(f"Número: {habitacion[0]}, Tipo: {habitacion[1]}, Estado: {habitacion[2]}")
        else:
            print("No hay habitaciones disponibles.")
        cerrar_conexion(conexion)

# Función para cambiar el estado de una habitación
def cambiar_estado_habitacion(numero, nuevo_estado):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "UPDATE habitaciones SET estado = %s WHERE numero = %s"
        cursor.execute(query, (nuevo_estado, numero))
        conexion.commit()
        print(f"Estado de la habitación {numero} cambiado a '{nuevo_estado}'.")
        cerrar_conexion(conexion)

# Función para registrar un invitado
def registrar_invitado(nombre, documento, telefono):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = "INSERT INTO invitados (nombre, documento, telefono) VALUES (%s, %s, %s)"
        cursor.execute(query, (nombre, documento, telefono))
        conexion.commit()
        print(f"Invitado {nombre} registrado exitosamente.")
        cerrar_conexion(conexion)

# Función para generar factura
def generar_factura(nombre_invitado):
    conexion = obtener_conexion()
    if conexion:
        cursor = conexion.cursor()
        query = """
        SELECT i.nombre, r.fecha_entrada, r.fecha_salida, r.estado
        FROM registros r
        JOIN invitados i ON r.id = i.registro_id
        WHERE i.nombre = %s
        """
        cursor.execute(query, (nombre_invitado,))
        factura = cursor.fetchone()
        if factura:
            print(f"Factura para {factura[0]}: Fecha Entrada: {factura[1]}, Fecha Salida: {factura[2]}, Estado: {factura[3]}")
        else:
            print(f"No se encontró un registro de factura para {nombre_invitado}.")
        cerrar_conexion(conexion)
