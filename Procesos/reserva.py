class Reserva:
    def __init__(self, id, FechaInicio, FechaFin, Estado):
        self.id = id
        self.FechaInicio = FechaInicio 
        self.FechaFin = FechaFin    
        self.Estado = Estado

    
    def RealizaReserva(self,id):
        id = input['Ingrese identificador de reserva: ']
        Reserva_Realizada = print('Reserva realizada con exito')
        return Reserva_Realizada + 'con id: ' + id
    
    def CancelaReserva(self,id):
        id = input['Ingrese identificador de reserva: ']        #Mismo metodo pero diferente accion
        pass
    
