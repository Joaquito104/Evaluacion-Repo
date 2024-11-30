import datetime as tiempo  # Importación de métodos de fechas

class Pago:
    def __init__(self, id, monto, FechaPago, MetodoPago):
        self.id = id
        self.monto = monto
        self.FechaPago = FechaPago
        self.MetodoPago = MetodoPago

    def ProcesarPago(self, monto_pago): 
        monto_pago = int(input('Para comenzar la transacción ingrese Monto: '))
        Selector = int(input("Seleccione el método de pago con el número correspondiente: \n 1 = Tarjeta de crédito \n 2 = Efectivo \n 3 = Transferencia Electrónica "))

        fecha_actual = tiempo.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Formato de hora: Año-Mes-Día - Hora:Minuto:Segundo

        if Selector == 1:
            identificador = input('Escriba el código de identificación del pago: ')
            MetodoDePago = 'Tarjeta de crédito'
            while True:
                Confirmar = input("Confirmar transacción con un Si/No respectivamente: ")  # Confirmar transacción

                if Confirmar.lower() == 'si':
                    self.id = identificador
                    self.monto = monto_pago
                    self.FechaPago = fecha_actual  # Guardar en la clase
                    self.MetodoPago = MetodoDePago

                    print(f'Transacción completada con id {self.id}, un monto total de {self.monto} con fecha {self.FechaPago} realizada con {self.MetodoPago}')  
                    break
                elif Confirmar.lower() == 'no':             # COMPLETAR
                    print('Transacción cancelada')
                    break
                else:
                    print('Error. Vuelva a confirmar la transacción')

        elif Selector == 2:
            pass                            #COMPLETAR

        elif Selector == 3:             
            pass                            #COMPLETAR
        else:
            print('Error, pago no aceptado. Vuelva a ingresar el método de pago')
