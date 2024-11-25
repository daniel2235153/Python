#EJ5:Diseñe un programa que tenga varias funciones, entre estas un menú para seleccionar que operación se debe realizar. 
# Elabore funciones que nos permita calcular: la suma, resta, multiplicación, división, potencia, porcentaje y raices.
#  Según la operación su programa debe permitir un número N de operaciones. 
def sumar():
    n = int(input("¿Cuántos números quiere sumar? "))
    total = 0
    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        total += num
    print(f"Resultado de la suma: {total}\n")


def restar():
    n = int(input("¿Cuántos números quieres restar? "))
    total = float(input("Ingrese el primer número: "))
    for i in range(1, n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        total -= num
    print(f"Resultado de la resta: {total}\n")


def multiplicar():
    n = int(input("¿Cuántos números quieres multiplicar? "))
    total = 1
    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        total *= num
    print(f"Resultado de la multiplicación: {total}\n")


def dividir():
    n = int(input("¿Cuántos números quieres dividir? "))
    total = float(input("Ingrese el primer número: "))
    for i in range(1, n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        if num == 0:
            print("Error: División por cero no permitida.")
            return
        total /= num
    print(f"Resultado de la división: {total}\n")
def potencia():
    base = float(input("Ingrese la base: "))
    exponente = float(input("Ingrese el exponente: "))
    resultado = base ** exponente
    print(f"Resultado de la potencia: {resultado}\n")

def porcentaje():
    total = float(input("Ingrese el total: "))
    porcentaje = float(input("Ingrese el porcentaje (sin el %): "))
    resultado = (total * porcentaje) / 100
    print(f"Resultado del porcentaje: {resultado}\n")

def raiz():
    n = int(input("¿Cuántas raíces deseas calcular? "))
    for i in range(n):
        num = float(input(f"Ingrese el número {i + 1}: "))
        if num < 0:
            print("Error: No se puede calcular la raíz de un número negativo.")
            continue
        resultado = num ** 0.5
        print(f"Raíz cuadrada de {num}: {resultado}\n")

def menu():
    while True:
        print('''Seleccione una operación:")
        1. Sumar
        2. Restar
        3. Multiplicar
        4. Dividir
        5. Potencia
        6. Porcentaje
        7. Raíces
        8. Salir''')

        opcion = int(input("Ingrese su opción: "))
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        elif opcion == 5:
            potencia()
        elif opcion == 6:
            porcentaje()
        elif opcion == 7:
            raiz()
        elif opcion == 8:
            break
        else:
            print("Opción no válida. Intente de nuevo.\n")
menu()
