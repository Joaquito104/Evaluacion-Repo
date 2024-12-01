from Personas.recepcionista import p
class Registro:
    def __init__(self, id, fechaEntrada, fechaSalida, estado):
        self.id = id
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.estado = estado
        self.invitado = None
        self.habitacion = None

    def agregar_invitado(self, invitado):
        self.invitado = invitado
    def registrar_pago(self, monto):
        if self.estado == 'reservado':
            print(f"Registro de pago de {monto} para el invitado {self.invitado.nombre}.")
            self.estado = 'pagado'  
        else:
            print("No se puede registrar el pago, el estado actual no lo permite.")


#Importar pagos, datos de reserva y mas

#Este archivo guardara registros de reserva, habitaciones y mas