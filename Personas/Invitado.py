import datetime
from Procesos.pago import pago as Plata #Importe clase pago y metodo
class Invitado:
    def __init__(self, nombre, id, telefono, direccion, habitacion):
        self.nombre = nombre
        self.id = id
        self.telefono = telefono
        self.direccion = direccion
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio.strptime(fecha_inicio, "año-mes-dia")  # type: ignore
        self.fecha_fin = datetime.strptime(fecha_fin, "año-mes-dia") # type: ignore
        self.pago = Plata

    def FechaInicio(self):
        self.fecha_inicio = datetime.strptime(fecha_inicio, "año-mes-dia") # type: ignore
        
    def FechaFin(self):
        self.fecha_fin = datetime.strptime(fecha_fin, "año-mes-dia") # type: ignore
        pass

    def duracion_estadia(self):
        return (self.fecha_fin - self.fecha_inicio).dias

    def Pago(self, costo_por_noche):
        duracion = self.duracion_estadia()
        costo_total = duracion * costo_por_noche
        return self.pago >= costo_total
    
print(f"Duración de la estadia: {Invitado.duracion_estadia()} días")
print(f"El costo total es correcto? {'Sí' if Invitado.es_pago_correcto(10000) else 'No'}")

 