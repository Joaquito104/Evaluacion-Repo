import datetime as tiempo
from Metodos.pago import Pago

class Invitado:
    def __init__(self, nombre, id, telefono, direccion, habitacion):
        self.nombre = nombre
        self.id = id
        self.habitacion = habitacion
        self.inicio = self.FechaInicio()
        self.fin = None
        self.pago = None  # Se inicializa el atributo de pago

    def FechaInicio(self):
        """Obtiene la fecha actual como string."""
        fecha_actual = tiempo.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return fecha_actual

    def FechaFin(self):
        """Solicita y valida la fecha de fin de la estancia."""
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
        """Calcula la duración de la estadía."""
        if self.fin:
            fecha_inicio = tiempo.datetime.strptime(self.inicio, "%Y-%m-%d %H:%M:%S")
            diferencia = self.fin - fecha_inicio
            return diferencia.days
        else:
            print("Fecha de fin no definida.")
            return 0

    def Pago(self, costo_por_noche):
        """Calcula el costo total de la estadía."""
        duracion = self.duracion_estadia()
        costo_total = duracion * costo_por_noche
        self.pago = Pago(costo_total)  # Creamos una instancia de Pago con el monto
        return costo_total
