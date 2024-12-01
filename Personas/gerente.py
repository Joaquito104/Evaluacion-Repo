#Archivo excluido del main unicamente accedido por el gerente

class Gerente:
    def __init__(self, nombre, idGerente, telefono):
        self.nombre=nombre
        self.idGerente=idGerente
        self.telefono=telefono
          
    def agregar_recepcionista(self, recepcionista):
        self.recepcionista_list.append(recepcionista)
        pass

    def eliminar_recepcionista (self, recepcionista):
        pass