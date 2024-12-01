class Habitacion:
    def __init__(self, numero, tipo, precio, disponibilidad):
        self.numero = numero    # El número es el identificador
        self.tipo = tipo
        self.precio = precio
        self.disponibilidad = disponibilidad

    def validador_numero(self, numero):
        # Validar que el número sea un entero
        try:
            numero = int(numero)
            return numero
        except ValueError:
            print('Error: El dato indicado no corresponde a un número entero.')
            return 0

    def ver_datos_habitacion(self):
        #Ver cada dato de la habitacion
        numero_habitacion = input ('Ingrese numero habitacion que necesite ver:')
        numero_habitacion = self.validador_numero(numero_habitacion)

        if numero_habitacion != 0 and numero_habitacion == self.numero:
            print(f'Número: {self.numero}, Tipo: {self.tipo}, Precio: {self.precio}, Disponibilidad: {self.disponibilidad}')

    def ver_estado(self):
        # Ver el estado de una habitación
        ver = input('Escriba el número de la habitación que quiere ver su estado: ')
        ver = self.validador_numero(ver)                          
        
        if ver is not 0 and ver == self.numero:
            print(f'El estado de la habitación {self.numero} es {self.disponibilidad}')
        else:
            print(f'No existe una habitación con el número {ver}.')

    def cambiar_estado(self):
        # Cambiar el estado de la habitación
        nuevo_estado = input('Seleccione el cambio de estado con el número correspondiente: \n 1.- Disponible \n 2.- Ocupado \n 3.- No cambiar: ')

        # Validacion
        nuevo_estado = self.validador_numero(nuevo_estado)
    
        if nuevo_estado is not 0:  # Solo proceder si el valor es válido
       
            numero = input('Ingrese el número de habitación para cambiar su estado: ')
            numero = self.validador_numero(numero)  # Validar

            if numero is not 0: #Proceder si el número también es válido
                
                if nuevo_estado == 1:
                    estado = 'Disponible'
                    self.disponibilidad = estado
                    print(f"Estado de la habitación {numero} cambiado a {self.disponibilidad}.")  

                elif nuevo_estado == 2:
                    estado = 'Ocupado'
                    self.disponibilidad = estado
                    print(f"Estado de la habitación {numero} cambiado a {self.disponibilidad}.")
                elif nuevo_estado == 3:
                    print(f"No se ha realizado ningún cambio en el estado de la habitación {numero}.")
        
                else:
                    print('Opción no válida. No se cambió el estado.')
            else:
                print("Número de habitación no válido.")
        else:
            print("Opción de estado no válida.")

