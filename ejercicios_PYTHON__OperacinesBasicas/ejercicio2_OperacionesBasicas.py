#Diseñe un programa empleando Python donde pueda realizar las operaciones básicas matemáticas
#  (suma, resta, multiplicación, división, raices, potencia y porcentajes).
#  Su programa debe mostrar todas las operaciones y a medida que va mostrando en pantalla los
#  resultados debe solicitar los siguientes datos sucesivamente. 
import math

while True:
    print("\nSeleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Raíz cuadrada")
    print("6. Potencia")
    print("7. Porcentaje")
    print("8. Salir")

    opcion = input("Ingrese el número de la operación que desea realizar: ")

    if opcion == "1":  
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {a} + {b} = {a + b}")

    elif opcion == "2":  
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {a} - {b} = {a - b}")

    elif opcion == "3":  
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        print(f"Resultado: {a} × {b} = {a * b}")

    elif opcion == "4":  
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        if b != 0:
            print(f"Resultado: {a} ÷ {b} = {a / b}")
        else:
            print("Error: División entre cero no permitida.")

    elif opcion == "5":  
        a = float(input("Ingrese el número: "))
        if a >= 0:
            print(f"Resultado: √{a} = {math.sqrt(a)}")
        else:
            print("Error: No se puede calcular la raíz cuadrada de un número negativo.")

    elif opcion == "6":  
        a = float(input("Ingrese la base: "))
        b = float(input("Ingrese el exponente: "))
        print(f"Resultado: {a}^{b} = {a ** b}")

    elif opcion == "7": 
        a = float(input("Ingrese el total: "))
        b = float(input("Ingrese el porcentaje: "))
        print(f"Resultado: {b}% de {a} = {a * (b / 100)}")

    elif opcion == "8":  
        print("Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("Opción no válida. Por favor, intente de nuevo.")
