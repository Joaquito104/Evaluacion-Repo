from Metodos.AccionesBD import agregar_habitacion
from Metodos.AccionesBD import ver_habitaciones
from Metodos.AccionesBD import cambiar_estado_habitacion
from Metodos.AccionesBD import registrar_invitado
from Metodos.AccionesBD import generar_factura

def menu_recepcionista():
    while True:
        print("\nMenú del Recepcionista:")
        print("1. Agregar habitación")
        print("2. Ver habitaciones")
        print("3. Cambiar estado de habitación")
        print("4. Registrar invitado")
        print("5. Generar factura")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            # Agregar nueva habitación
            numero = input("Ingrese el número de habitación: ")
            tipo = input("Ingrese el tipo de habitación: ")
            agregar_habitacion(numero, tipo)

        elif opcion == '2':
            # Ver todas las habitaciones
            ver_habitaciones()

        elif opcion == '3':
            # Cambiar estado de habitación
            numero = input("Ingrese el número de la habitación: ")
            estado = input("Ingrese el nuevo estado (Disponible / Ocupado): ")
            cambiar_estado_habitacion(numero, estado)

        elif opcion == '4':
            # Registrar invitado
            nombre = input("Ingrese el nombre del invitado: ")
            documento = input("Ingrese el documento de identidad del invitado: ")
            telefono = input("Ingrese el teléfono del invitado: ")
            registrar_invitado(nombre, documento, telefono)

        elif opcion == '5':
            # Generar factura
            nombre_invitado = input("Ingrese el nombre del invitado: ")
            generar_factura(nombre_invitado)

        elif opcion == '6':
            print("Saliendo del sistema.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")

# Llamamos a la función del menú
menu_recepcionista()

