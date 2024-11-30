from Personas.recepcionista import p
class Registro:
    def __init__(self, id, fechaEntrada, fechaSalida, estado):
        self.id = id
        self.fechaEntrada = fechaEntrada
        self.fechaSalida = fechaSalida
        self.estado = estado
        self.invitado = None
        self.habitacion = None


#Importar pagos, datos de reserva y mas

#Este archivo guardara registros de reserva, habitaciones y mas