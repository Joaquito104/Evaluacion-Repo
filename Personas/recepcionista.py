import Personas.Invitado
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


    def generar_factura(self, invitado):
        montoTotal = sum(registro.habitacion.precio for registro in invitado.registros_list)
        factura = factura(len(invitado.factura_list) + 1, "2023-10-10", montoTotal, "Pagada")
        factura.invitado = invitado
        factura.registros_list = invitado.registros_list
        invitado.factura_list.append(factura)
        print(f"Factura generada para {invitado.nombre}: Monto Total = {montoTotal}.")
      