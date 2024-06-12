# Elaborado por: Elías Ramírez Hernández y Lindsay Nahome Marín Sánchez
# Fecha de creación 31-05-2024 10:30am
# Última modificación: 03-06-2024 9:03pm
# Versión: 3.12.3

#Definición de clases

class Pokemon():
    nombre = ""
    tuplaMedidas= tuple()
    listaTipos = []
    puntos = 0
    esShiny = False
    imagen = ""

    def __init__(self):
        self.nombre = ""
        self.tuplaMedidas = tuple()
        self.listaTipos = []
        self.puntos = 0
        self.esShiny = False
        self.imagen = ""

    def asignarNombre(self, nombre):
        self.nombre = nombre

    def asignarTuplaMedidas(self,tuplaMedidas):
        self.tuplaMedidas = tuplaMedidas

    def asignarListaTipos(self, listaTipos):
        self.listaTipos = listaTipos

    def asignarPuntos(self, puntos):
        self.puntos = puntos

    def asignarEsShiny(self, esShiny):
        self.esShiny = esShiny

    def asignarImagen(self,imagen):
        self.imagen=imagen
        
    # Funciones de mostrar
    
    def mostrarNombre(self):
        return self.nombre

    def mostrarTuplaMedidas(self):
        return self.tuplaMedidas

    def mostrarListaTipos(self):
        return self.listaTipos

    def mostrarPuntos(self):
        return self.puntos

    def mostrarEsShiny(self):
        return self.esShiny

    def mostrarImagen(self):
        return self.imagen

    def mostrarTodo(self):
        return self.nombre,self.tuplaMedidas,self.listaTipos,self.puntos,self.esShiny,self.imagen
        
        