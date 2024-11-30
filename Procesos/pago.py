class Pago:
    def __init__(self, id, monto, FechaPago, MetodoPago):
        self.id = id
        self.monto = monto
        self.FechaPago = FechaPago
        self.MetodoPago = MetodoPago

    def Monto(self, monto) :
        monto = int(input('Ingrese Monto: '))
        return monto

    
    def ProcesarPago(self,MetodoPago):          #Completa esta funcion definida

        MetodoPago = int(input("Selecciones el metodo de pago con el numero correspondiente: \n 1 = Tarjeta de credito \n 2 = Efectivo : \n "))
        

        if MetodoPago == 1:
            
            pass

        elif MetodoPago == 2:
            pass

        else:
            print('Error pago no aceptado. Vuelva a Ingresar el metodo pago')

        return MetodoPago

