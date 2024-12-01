class Registro:
    def __init__(self, id, fechaEntrada, fechaSalida, estado):
        self.id = id
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.estado = estado
        self.invitado = None
        self.habitacion = None

class SistemaRegistro:
    def __init__(self):
        self.registros = []

    def agregar_registro(self, registro):
        self.registros.append(registro) 
        print(f"Registro agregado: ID {registro.id}, Entrada {registro.fechaEntrada}, Salida {registro.fechaSalida}, Estado {registro.estado}")

    def eliminar_registro(self, id):
        for registro in self.registros:
            if registro.id == id:
                self.registros.remove(registro)
                print(f"Registro eliminado: ID {registro.id}")
                return
        print(f"No se encontró un registro con ID: {id}")

    def buscar_registro(self, id):
        for registro in self.registros:
            if registro.id == id:
                print(f"Registro encontrado: ID {registro.id}, Entrada {registro.fechaEntrada}, Salida {registro.fechaSalida}, Estado {registro.estado}")
                return
        print(f"No se encontró un registro con ID: {id}")

    def mostrar_registros(self):
        if self.registros:
            for registro in self.registros:
                print(f"ID {registro.id}, Entrada {registro.fechaEntrada}, Salida {registro.fechaSalida}, Estado {registro.estado}")
        else:
            print("No hay registros para mostrar.")
        
    def agregar_invitado(self, id, invitado):
        for registro in self.registros:
            if registro.id == id:
                registro.invitado = invitado
                print(f"Invitado {invitado} agregado al registro con ID {id}")
                return
        print(f"No se encontró un registro con ID: {id}")

    def registrar_pago(self, id, monto):
        for registro in self.registros:
            if registro.id == id:
                if registro.estado == 'reservado':
                    print(f"Pago de {monto} registrado para el invitado {registro.invitado} en el registro con ID {id}.")
                    registro.estado = 'pagado'
                    return
                else:
                    print("El pago no puede ser registrado, el estado no lo permite.")
                    return
        print(f"No se encontró un registro con ID: {id}")
