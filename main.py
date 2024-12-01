from Hotelsito.habitacion import SistemaHabitaciones
from Personas.Invitado import registrar_invitado

def menu():
    sistema_habitaciones = SistemaHabitaciones()

    while True:
        print("\nMenú:")
        print("1. Agregar habitación")
        print("2. Ver habitaciones")
        print("3. Cambiar estado de habitación")
        print("4. Registrar invitado")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            sistema_habitaciones.agregar_habitacion()
        elif opcion == '2':
            sistema_habitaciones.ver_habitaciones()
        elif opcion == '3':
            sistema_habitaciones.cambiar_estado()
        elif opcion == '4':
            invitado = registrar_invitado(sistema_habitaciones)
            if invitado:
                print(f"El pago total para el invitado {invitado.nombre} es de {invitado.pago.monto} pesos.")
        elif opcion == '5':
            print("Saliendo...")
            break

# Ejecutar el menú
menu()
