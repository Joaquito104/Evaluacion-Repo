class Recepcionista:
    def __init__(self, nombre, idEmpleado, turno):
        self.nombre=nombre
        self.idEmpleado=idEmpleado
        self.turno=turno

    def gestionar_reserva(self, invitado, habitacion, fechaEntrada, fechaSalida):
        registro = registro(len(self.registros_list) + 1, fechaEntrada, fechaSalida, "Reservado")
        registro.invitado = invitado
        registro.habitacion = habitacion
        self.registros_list.append(registro)
        habitacion.registros_list.append(registro)
        invitado.registros_list.append(registro)
        print(f"Reserva realizada para {invitado.nombre} en la habitación {habitacion.numero}.")


      