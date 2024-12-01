#Menu para adicion de registros
#Accedido por el gerente y recepcionista

from Metodos.registros import Registro
from Metodos.registros import SistemaRegistro

def menu():
    sistema = SistemaRegistro()
    while True:
        print("\n--- Menú de Registro ---")
        print("1. Agregar registro")
        print("2. Eliminar registro")
        print("3. Buscar registro")
        print("4. Mostrar todos los registros")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            id = int(input("Ingrese el ID del registro: "))
            fechaEntrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
            fechaSalida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
            estado = input("Ingrese el estado del registro: ")
            registro = registro(id, fechaEntrada, fechaSalida, estado)
            sistema.agregar_registro(registro)

        elif opcion == "2":
            id = int(input("Ingrese el ID del registro a eliminar: "))
            sistema.eliminar_registro(id)

        elif opcion == "3":
            id = int(input("Ingrese el ID del registro a buscar: "))
            sistema.buscar_registro(id)

        elif opcion == "4":
            sistema.mostrar_registros()

        elif opcion == "5":
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

