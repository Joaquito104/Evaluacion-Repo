import datetime as tiempo
from Metodos.pago import Pago
from Hotelsito.habitacion import SistemaHabitaciones

class Invitado:
    def __init__(self, nombre, id, telefono, direccion, habitacion):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.habitacion = habitacion
        self.inicio = self.FechaInicio()
        self.fin = None
        self.pago = None  # Atributo para almacenar el pago

    def FechaInicio(self):
        """Obtiene la fecha y hora actuales."""
        fecha_actual = tiempo.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return fecha_actual

    def FechaFin(self):
        """Solicita al usuario ingresar la fecha de fin."""
        while True:
            try:
                dia = int(input('Ingrese el día (formato: DD): '))
                hora = int(input('Ingrese la hora (formato: HH): '))
                minuto = int(input('Ingrese los minutos (formato: MM): '))
            except ValueError:
                print('Error. El valor proporcionado es incorrecto.')
                continue
            break

        ahora = tiempo.datetime.now()
        año = ahora.year
        mes = ahora.month
        fecha = f"{año}-{mes:02d}-{dia:02d}-{hora:02d}-{minuto:02d}"
        self.fin = tiempo.datetime.strptime(fecha, "%Y-%m-%d-%H-%M")
        return self.fin

    def duracion_estadia(self):
        """Calcula la duración de la estadía en días."""
        if self.fin:
            fecha_inicio = tiempo.datetime.strptime(self.inicio, "%Y-%m-%d %H:%M:%S")
            diferencia = self.fin - fecha_inicio
            return diferencia.days
        else:
            print("Fecha de fin no definida.")
            return 0

    def Pago(self, costo_por_noche):
        """Calcula el costo total de la estadía del invitado."""
        duracion = self.duracion_estadia()
        costo_total = duracion * costo_por_noche
        print(f"El costo total es: {costo_total} pesos")
        return costo_total

    def realizar_pago(self, costo_por_noche):
        """Realiza el pago de la estadía del invitado."""
        costo_total = self.Pago(costo_por_noche)
        
        # Crear una instancia de Pago
        pago = Pago()
        pago.ProcesarPago()
        
        # Asociamos el pago con el invitado
        self.pago = pago
        print(f"El pago ha sido procesado para el invitado {self.nombre}.")

# Para realizar el pago y asociarlo a un invitado
def registrar_invitado(sistema_habitaciones):
    habitacion_elegida = sistema_habitaciones.obtener_habitacion_disponible()

    if not habitacion_elegida:
        print("No hay habitaciones disponibles.")
        return None

    # Recibir los datos del invitado
    nombre = input("Ingrese el nombre del invitado: ")
    id = input("Ingrese el ID del invitado: ")
    telefono = input("Ingrese el teléfono del invitado: ")
    direccion = input("Ingrese la dirección del invitado: ")

    # Crear un nuevo objeto Invitado
    invitado = Invitado(nombre, id, telefono, direccion, habitacion_elegida)

    # Cambiar el estado de la habitación a 'Ocupado'
    habitacion_elegida.cambiar_estado("Ocupado")
    print(f"Invitado {nombre} registrado exitosamente en la habitación {habitacion_elegida.numero}.")

    # Realizar el pago
    invitado.realizar_pago(habitacion_elegida.precio)

    return invitado
