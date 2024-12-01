#Menu Exclusivo Recepcionistas
from Hotelsito.habitacion import SistemaHabitaciones
from Personas.recepcionista import Recepcionista

def menu():
    sistema_habitaciones = SistemaHabitaciones()
    recepcionista = Recepcionista()

    while True:
        print("\nMenú:")
        print("1. Agregar habitación")
        print("2. Ver habitaciones")
        print("3. Cambiar estado de habitación")
        print("4. Registrar invitado")
        print("5. Generar factura")
        print("6. Salir")

        try:
            opcion = input("Seleccione una opción: ")
            if opcion == '1':
                sistema_habitaciones.agregar_habitacion()
            elif opcion == '2':
                sistema_habitaciones.ver_habitaciones()
            elif opcion == '3':
                numero = int(input("Ingrese el número de la habitación para cambiar su estado: "))
                nuevo_estado = input("Ingrese el nuevo estado (Disponible / Ocupado): ").capitalize()
                sistema_habitaciones.cambiar_estado(numero, nuevo_estado)
            elif opcion == '4':
                invitado = recepcionista.gestionar_reserva(sistema_habitaciones)
                if invitado:
                    print(f"El pago total para el invitado {invitado.nombre} es de {invitado.pago.monto} pesos.")
            elif opcion == '5':
                if invitado:
                    recepcionista.generar_factura(invitado)
            elif opcion == '6':
                print("Saliendo...")
                break

        except ValueError:
            print('Error Saliendo del sistema')
            break

# Ejecutar el menú
menu()
