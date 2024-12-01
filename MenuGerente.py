import Metodos.registros  
from Metodos.registros import SistemaRegistro, Registro  
from Personas.gerente import Gerente  

def menu():
    sistema = SistemaRegistro()  # Instanciamos el sistema de registros
    while True:
        print("\n--- Menú de Gerente ---")
        print("1. Agregar registro")
        print("2. Eliminar registro")
        print("3. Buscar registro")
        print("4. Mostrar todos los registros")
        print("5. Agregar invitado a un registro")
        print("6. Registrar pago")
        print("7. Cambiar estado de registro")
        print("8. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para agregar un nuevo registro
            id = int(input("Ingrese el ID del registro: "))
            fechaEntrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
            fechaSalida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
            print("Seleccione el estado del registro:")
            print("1. Usando habitación")
            print("2. Sin habitación")
            estado_opcion = input("Seleccione una opción: ")
            if estado_opcion == "1":
                estado = "Usando habitación"
            else:
                estado = "Sin habitación"
            registro = Registro(id, fechaEntrada, fechaSalida, estado)  # Crear el nuevo registro
            sistema.agregar_registro(registro)  # Usar el método para agregarlo al sistema
            print(f"Registro con ID {id} agregado exitosamente.")

        elif opcion == "2":
            # Opción para eliminar un registro por ID
            id = int(input("Ingrese el ID del registro a eliminar: "))
            sistema.eliminar_registro(id)  # Usar el método para eliminar el registro
            print(f"Registro con ID {id} eliminado exitosamente.")

        elif opcion == "3":
            # Opción para buscar un registro por ID
            id = int(input("Ingrese el ID del registro a buscar: "))
            sistema.buscar_registro(id)  # Usar el método para buscar el registro
            print(f"Busqueda del registro con ID {id} realizada exitosamente.")

        elif opcion == "4":
            # Opción para mostrar todos los registros
            sistema.mostrar_registros()  # Usar el método para mostrar todos los registros
            print("Lista de registros mostrada exitosamente.")

        elif opcion == "5":
            # Opción para agregar un invitado a un registro
            id = int(input("Ingrese el ID del registro al que desea agregar un invitado: "))
            invitado = input("Ingrese el nombre del invitado: ")
            sistema.agregar_invitado(id, invitado)  # Usar el método para agregar un invitado
            print(f"Invitado '{invitado}' agregado exitosamente al registro con ID {id}.")

        elif opcion == "6":
            # Opción para registrar un pago en un registro
            id = int(input("Ingrese el ID del registro para registrar el pago: "))
            monto = float(input("Ingrese el monto del pago: "))
            sistema.registrar_pago(id, monto)  # Usar el método para registrar el pago
            print(f"Pago de {monto} registrado exitosamente en el registro con ID {id}.")

        elif opcion == "7":
            # Opción para cambiar el estado de un registro
            id = int(input("Ingrese el ID del registro al que desea cambiar el estado: "))
            print("Seleccione el nuevo estado del registro:")
            print("1. Usando habitación")
            print("2. Sin habitación")
            estado_opcion = input("Seleccione una opción: ")
            if estado_opcion == "1":
                estado = "Usando habitación"
            else:
                estado = "Sin habitación"
            sistema.cambiar_estado(id, estado)  # Usamos el método para cambiar el estado
            print(f"Estado del registro con ID {id} cambiado exitosamente a '{estado}'.")

        elif opcion == "8":
            print("Saliendo del sistema.")
            break  # Salir del bucle y terminar el programa

        else:
            print("Opción no válida. Intente de nuevo.")  # Mensaje en caso de opción inválida

# Llamamos a la función del menú para ejecutar el sistema
menu()
