class Habitacion:
    def __init__(self, id, numero, tipo, precio, disponibilidad):
        self.id = id
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad

    def cambiar_estado(self, nuevo_estado):
        self.estado = nuevo_estado
        print(f"Estado de la habitación {self.numero} cambiado a {nuevo_estado}.")
