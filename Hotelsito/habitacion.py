class Habitacion:
    def __init__(self, numero, tipo, precio, disponibilidad):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad

    def cambiar_estado(self, nuevo_estado):
        """Cambia el estado de la habitación."""
        if nuevo_estado in ["Disponible", "Ocupado"]:
            self.disponibilidad = nuevo_estado
            print(f"Estado de la habitación {self.numero} cambiado a {nuevo_estado}.")
        else:
            print("Estado no válido. Debe ser 'Disponible' o 'Ocupado'.")

class SistemaHabitaciones:
    def __init__(self):
        self.habitaciones = []

    def agregar_habitacion(self):
        """Agrega una nueva habitación al sistema."""
        try:
            numero = int(input("Ingrese número de habitación: "))
            tipo = input("Ingrese Tipo (Sencilla, Doble, etc.): ")
            precio = float(input("Ingrese el precio de la habitación por noche: "))
            if precio <= 0:
                print("Error: El precio debe ser mayor que 0.")
                return

            habitacion = Habitacion(numero, tipo, precio, "Disponible")
            self.habitaciones.append(habitacion)
            print("Habitación agregada exitosamente.")
        except ValueError:
            print("Error: Entrada inválida. Asegúrese de ingresar un número válido para el precio y el número de habitación.")

    def ver_habitaciones(self):
        """Muestra todas las habitaciones registradas."""
        if self.habitaciones:
            for habitacion in self.habitaciones:
                print(f"Número: {habitacion.numero}, Tipo: {habitacion.tipo}, Precio: {habitacion.precio}, Disponibilidad: {habitacion.disponibilidad}")
        else:
            print("No hay habitaciones registradas.")

    def cambiar_estado(self, numero, nuevo_estado):
        """Permite cambiar el estado de una habitación dado su número y el nuevo estado."""
        if nuevo_estado != "Disponible" and nuevo_estado != "Ocupado":
            print("Estado no válido. Debe ser 'Disponible' o 'Ocupado'.")
            return

        
        for habitacion in self.habitaciones:
            if habitacion.numero == numero:
                habitacion.cambiar_estado(nuevo_estado)
                return
        
        print("Habitación no encontrada.")
