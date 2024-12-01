from Metodos.AccionesBD import agregar_registro
from Metodos.AccionesBD import eliminar_registro
from Metodos.AccionesBD import buscar_registro
from Metodos.AccionesBD import mostrar_registros
from Metodos.AccionesBD import registrar_pago
from Metodos.AccionesBD import cambiar_estado

def menu_registro():
    while True:
        print("\n--- Menú de Registros ---")
        print("1. Agregar registro")
        print("2. Eliminar registro")
        print("3. Buscar registro")
        print("4. Mostrar todos los registros")
        print("5. Registrar pago")
        print("6. Cambiar estado de registro")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Opción para agregar un nuevo registro
            fechaEntrada = input("Ingrese la fecha de entrada (YYYY-MM-DD): ")
            fechaSalida = input("Ingrese la fecha de salida (YYYY-MM-DD): ")
            estado = input("Ingrese el estado del registro (Usando habitación / Sin habitación): ")
            agregar_registro(fechaEntrada, fechaSalida, estado)

        elif opcion == "2":
            # Opción para eliminar un registro por ID
            id = int(input("Ingrese el ID del registro a eliminar: "))
            eliminar_registro(id)

        elif opcion == "3":
            # Opción para buscar un registro por ID
            id = int(input("Ingrese el ID del registro a buscar: "))
            buscar_registro(id)

        elif opcion == "4":
            # Opción para mostrar todos los registros
            mostrar_registros()

        elif opcion == "5":
            # Opción para registrar un pago
            id = int(input("Ingrese el ID del registro para registrar el pago: "))
            monto = float(input("Ingrese el monto del pago: "))
            registrar_pago(monto, id)

        elif opcion == "6":
            # Opción para cambiar el estado de un registro
            id = int(input("Ingrese el ID del registro al que desea cambiar el estado: "))
            nuevo_estado = input("Ingrese el nuevo estado (Usando habitación / Sin habitación): ")
            cambiar_estado(id, nuevo_estado)

        elif opcion == "7":
            print("Saliendo del sistema.")
            break  # Salir del bucle y terminar el programa

        else:
            print("Opción no válida. Intente de nuevo.")

# Llamamos a la función del menú
menu_registro()
