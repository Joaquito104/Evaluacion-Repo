import datetime as tiempo

class Pago:
    def __init__(self, monto):
        self.monto = monto
        self.MetodoPago = None

    def confirmar_transaccion(self, monto_pago, MetodoDePago):
        while True:
            confirmar = input("Confirmar transacción con un Si/No respectivamente: ")

            if confirmar.lower() == 'si':
                self.MetodoPago = MetodoDePago
                print(f'Transacción completada con un monto total de {self.monto} realizado con {self.MetodoPago}')
                break

            elif confirmar.lower() == 'no':
                print('Transacción cancelada')
                break

            else:
                print('Error. Vuelva a confirmar la transacción')

    def procesar_pago(self):
        monto_pago = float(input('Ingrese el monto del pago: '))
        while True:
            selector = int(input("Seleccione el método de pago (1 = Tarjeta de crédito, 2 = Efectivo, 3 = Transferencia): "))
            
            if selector == 1:
                metodo_pago = 'Tarjeta de crédito'
                self.confirmar_transaccion(monto_pago, metodo_pago)
                break
            elif selector == 2:
                metodo_pago = 'Efectivo'
                self.confirmar_transaccion(monto_pago, metodo_pago)
                break
            elif selector == 3:
                metodo_pago = 'Transferencia Electrónica'
                self.confirmar_transaccion(monto_pago, metodo_pago)
                break
            else:
                print('Método de pago no válido.')
