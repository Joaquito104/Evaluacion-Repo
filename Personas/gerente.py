#Archivo excluido del main.
#Unicamente accedido por el gerente

class Gerente:
    def __init__(self, nombre, idGerente, telefono, departamento):
        self.nombre=nombre
        self.idGerente=idGerente
        self.telefono=telefono
        self.departamento = departamento
        self.recepcionistas = []#supervisar a los recepcionistas
        self.reportes = []#generar reportes de los estados del hotel
          
    def agregar_recepcionista(self, recepcionista):
        self.recepcionista_list.append(recepcionista)
        print(f"Recepcionista {recepcionista} agregado.")
    
    def supervisar_personal(self):
        print("Supervisando al personal de recepción:")
        for recepcionista in self.recepcionistas:
            print(f"- {recepcionista}")

    def generar_reporte(self, ocupacion, ingresos, disponibilidad):
        """Genera un reporte sobre el estado del hotel."""
        reporte = {
            'ocupacion': ocupacion,
            'ingresos': ingresos,
            'disponibilidad': disponibilidad
        }
        self.reportes.append(reporte)
        print("Reporte generado:")
        print(reporte)

    def gestionar_personal(self):
        print("Gestionando el personal del hotel.")
        while True:
            print("\nOpciones de gestión del personal:")
            print("1. Contratar recepcionista")
            print("2. Despedir recepcionista")
            print("3. Actualizar información de recepcionista")
            print("4. Mostrar todos los recepcionistas")
            print("5. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                nombre = input("Ingrese el nombre del recepcionista: ")
                self.agregar_recepcionista(nombre)

            elif opcion == "2":
                nombre = input("Ingrese el nombre del recepcionista a despedir: ")
                if nombre in self.recepcionistas:
                    self.recepcionistas.remove(nombre)
                    print(f"Recepcionista {nombre} despedido.")
                else:
                    print(f"Recepcionista {nombre} no encontrado.")

            elif opcion == "3":
                nombre = input("Ingrese el nombre del recepcionista a actualizar: ")
                if nombre in self.recepcionistas:
                    nuevo_nombre = input("Ingrese el nuevo nombre: ")
                    index = self.recepcionistas.index(nombre)
                    self.recepcionistas[index] = nuevo_nombre
                    print(f"Recepcionista {nombre} actualizado a {nuevo_nombre}.")
                else:
                    print(f"Recepcionista {nombre} no encontrado.")

            elif opcion == "4":
                self.supervisar_personal()

            elif opcion == "5":
                print("Saliendo de la gestión del personal.")
                break

            else:
                print("Opción no válida. Intente de nuevo.")
           
  