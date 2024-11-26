'''
Haga un programa que tenga las siguientes clases:

1. Uisbarbosa
2. Vigilancia
3. Administrativos
4. Auxiliares  

En estas se pediran los siguientes atributos:
Nombre, Documento, Fecha de nacimiento, Profesion, Turno, Dependencia, Función, Horas trabajadas, Lugar, Salario

Dependiendo de cada clase use herencia
'''
import datetime

def edad_persona(fecha):
    d = datetime.datetime.strptime(fecha, '%d/%m/%Y')
    hoy = datetime.datetime.now()
    edad = hoy.year - d.year
    if hoy.month < d.month or (hoy.month == d.month and hoy.day < d.day):
        edad -= 1
    return edad

# Clase base Uisbarbosa
class Uisbarbosa:
    def __init__(self):
        self.nombre = input('Ingrese su nombre: ')
        self.documento = input('Ingrese su documento: ')
        self.naci = input('Ingrese su fecha de nacimiento (DD/MM/AAAA): ')
        self.edad = edad_persona(self.naci)
        self.profe = input('Ingrese su profesion: ')
        self.ht = float(input('Ingrese sus horas trabajadas: '))

    def imprimir(self):
        print(f'Su nombre es {self.nombre}, y su edad es {self.edad} años.\n'
              f'Su documento es {self.documento}, su fecha de nacimiento es {self.naci}, '
              f'su profesion es {self.profe} y sus horas trabajadas son {self.ht}')

# Clase Vigilancia, que hereda de Uisbarbosa
class Vigilancia(Uisbarbosa):
    def __init__(self):
        super().__init__()
        self.turno = input('Ingrese su turno: ')
        self.lugar = input('Ingrese su lugar: ')

    def sueldo(self):
        self.salario = self.ht * 50000
        print(f'Su salario es de: {self.salario}')

    def imprimir(self):
        super().imprimir()
        print(f'Su turno es {self.turno}, su lugar es {self.lugar}, y su salario es de {self.salario}')

# Clase Administrativos, que hereda de Uisbarbosa
class Administrativos(Uisbarbosa):
    def __init__(self):
        super().__init__()
        self.dep = input('Ingrese su dependencia: ')

    def sueldo(self):
        self.salario = self.ht * 75000
        print(f'Su salario es de: {self.salario}')

    def funciones(self):
        self.funcion = input('Ingrese su función: ')
        print(f'Su función es: {self.funcion}')

    def imprimir(self):
        super().imprimir()
        print(f'Su dependencia es {self.dep}, y su salario es de {self.salario}')

# Clase Auxiliares, que hereda de Vigilancia
class Auxiliares(Vigilancia):
    def __init__(self):
        super().__init__()

    def funciones(self):
        self.funcion = input('Ingrese su función: ')
        print(f'Su función es: {self.funcion}')

# Función principal para interactuar con las clases
def menu():
    while True:
        print("\nSeleccione una opción:")
        print("1. Crear Uisbarbosa")
        print("2. Crear Vigilancia")
        print("3. Crear Administrativos")
        print("4. Crear Auxiliares")
        print("5. Salir")
        
        opcion = input("Opción: ")

        if opcion == '1':
            persona = Uisbarbosa()
            persona.imprimir()
        elif opcion == '2':
            vigilancia = Vigilancia()
            vigilancia.sueldo()
            vigilancia.imprimir()
        elif opcion == '3':
            administrativo = Administrativos()
            administrativo.sueldo()
            administrativo.funciones()
            administrativo.imprimir()
        elif opcion == '4':
            auxiliar = Auxiliares()
            auxiliar.funciones()
            auxiliar.imprimir()
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente nuevamente.")

# Llamar a la función principal para ejecutar el menú
menu()
