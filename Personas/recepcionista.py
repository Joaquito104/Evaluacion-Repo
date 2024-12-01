from Personas.invitado import Invitado
from Metodos.pago import Pago
from Hotelsito.habitacion import SistemaHabitaciones

class Recepcionista:
    def __init__(self):
        pass

    def gestionar_reserva(self, sistema_habitaciones):
        """Gestiona la reserva de un invitado."""
        nombre = input("Ingrese el nombre del invitado: ")
        id = input("Ingrese el ID del invitado: ")
        telefono = input("Ingrese el teléfono del invitado: ")
        direccion = input("Ingrese la dirección del invitado: ")

        # Selecciona una habitación disponible
        habitacion = sistema_habitaciones.obtener_habitacion_disponible()
        if habitacion:
            print(f"Se asignó la habitación {habitacion.numero} al invitado.")
            # Crear el invitado y manejar las fechas
            invitado = Invitado(nombre, id, telefono, direccion, habitacion.numero)
            gestionar_inicio = invitado.FechaInicio()
            gestionar_fin = invitado.FechaFin()

            print(f'Inicio de reserva con ID {id} desde {gestionar_inicio} y finalizando en {gestionar_fin}')
            return invitado
        else:
            print("No hay habitaciones disponibles.")
            return None

    def generar_factura(self, invitado):
        """Genera la factura para un invitado."""
        costo_por_noche = float(input("Ingrese el costo por noche: "))
        total_pago = invitado.Pago(costo_por_noche)
        
        # Procesamos el pago
        invitado.pago.procesar_pago()
        
        # Muestra la factura
        print(f"\nFactura de invitado {invitado.nombre}:")
        print(f"ID: {invitado.id}")
        print(f"Teléfono: {invitado.telefono}")
        print(f"Dirección: {invitado.direccion}")
        print(f"Fecha de inicio: {invitado.inicio}")
        print(f"Fecha de fin: {invitado.fin}")
        print(f"Costo total por la estadía: {total_pago} pesos")
        print(f"Método de pago: {invitado.pago.MetodoPago}")
