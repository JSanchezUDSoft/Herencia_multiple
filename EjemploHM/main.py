
#Herencia multiple

class Estudiante:
    def __init__(self):
        pass
    def estudiar(self):
        print('Estudiando')
    def tarea(self):
        print('Haciendo tarea')

class Trabajador:
    def __init__(self):
        pass
    def trabajar(self):
        print('Trabajando')

class Nino:
    def __init__(self):
        pass
    def jugar(self):
        print('Jugando')
    def comer(self):
        print('Comiendo')

class Deportista:
    def __init__(self):
        pass
    def entrenar(self):
        print('Entrenando')
    def competir(self):
        print('Compitiendo')


class Persona(Estudiante,Trabajador,Nino,Deportista):
    def __del__(self):
        print('Persona')
persona1 = Persona()
print(persona1.tarea())
print(persona1.estudiar())
print(persona1.comer())
print(persona1.jugar())
print(persona1.entrenar())
print(persona1.trabajar())

