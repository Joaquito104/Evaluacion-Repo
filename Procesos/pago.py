import datetime as tiempo  # Importación de métodos de fechas

class Pago:
    def __init__(self, id=None, monto=None, FechaPago=None, MetodoPago=None):
        self.id = id
        self.monto = monto
        self.FechaPago = FechaPago
        self.MetodoPago = MetodoPago

    def confirmar_transaccion(self, identificador, monto_pago, fecha_actual, MetodoDePago):
        while True:
            Confirmar = input("Confirmar transacción con un Si/No respectivamente: ")  # Confirmar transacción

            if Confirmar.lower() == 'si':
                self.id = identificador
                self.monto = monto_pago
                self.FechaPago = fecha_actual  # Guardar en la clase
                self.MetodoPago = MetodoDePago
                print(f'Transacción completada con id {self.id}, un monto total de {self.monto} con fecha {self.FechaPago} realizada con {self.MetodoPago}')  
                break  # Salir del bucle de confirmaión 
            
            elif Confirmar.lower() == 'no':           
                print('Transacción cancelada')
                break  # Salir del bucle de confirmación

            else:
                print('Error. Vuelva a confirmar la transacción')

    def ProcesarPago(self): 
        monto_pago = int(input('Para comenzar la transacción ingrese Monto: '))

        fecha_actual = tiempo.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato de hora: Año-Mes-Día - Hora:Minuto:Segundo

        while True:
            Selector = int(input("Seleccione el método de pago con el número correspondiente: \n 1 = Tarjeta de crédito \n 2 = Efectivo \n 3 = Transferencia Electrónica "))
            
            if Selector == 1:
                identificador1 = input('Escriba el código de identificación del pago: ')
                MetodoDePago = 'Tarjeta de crédito'
                self.confirmar_transaccion(identificador1, monto_pago, fecha_actual, MetodoDePago)
                break  # Salir del bucle después de completar la transacción

            elif Selector == 2:
                identificador2 = input('Escriba el código de identificación del pago: ')
                MetodoDePago = 'Efectivo'
                self.confirmar_transaccion(identificador2, monto_pago, fecha_actual, MetodoDePago)
                break  # Salir del bucle después de completar la transacción

            elif Selector == 3:
                identificador3 = input('Escriba el código de identificación del pago: ')
                MetodoDePago = 'Transferencia Electrónica'
                self.confirmar_transaccion(identificador3, monto_pago, fecha_actual, MetodoDePago)
                break  # Salir del bucle después de completar la transacción

            else:
                print('Error, pago no aceptado. Vuelva a ingresar el método de pago')
