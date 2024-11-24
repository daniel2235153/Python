#EJ.2 Construir un programa que calcule y muestre por pantalla las  raíces de la ecuación de segundo grado de coeficientes reales. El programa debe 
#diferenciar los diferentes casos que puedan surgir: la existencia de dos raíces reales distintas, de dos raíces reales iguales y de dos raíces complejas. 
#Nota: se recomienda el empleo de sentencias if_else [Ecuacion cuadratica]

import math as m

a = float(input('Ingrese el valor de a: '))
b = float(input('Ingrese el valor de b: '))
c = float(input('Ingrese el valor de c: '))

if a == 0:
    print("El valor de 'a' no puede ser cero. Esto no es una ecuación cuadrática.")
else:
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + m.sqrt(discriminante)) / (2 * a)
        raiz2 = (-b - m.sqrt(discriminante)) / (2 * a)
        print(f"Las raíces son reales y distintas: {raiz1:.2f} y {raiz2:.2f}")
    elif discriminante == 0:
        raiz = -b / (2 * a)
        print(f"Las raíces son reales e iguales: {raiz:.2f}")
    else:
        parte_real = -b / (2 * a)
        parte_imaginaria = m.sqrt(abs(discriminante)) / (2 * a)
        print(f"Las raíces son complejas:")
        print(f"{parte_real:.2f} + {parte_imaginaria:.2f}i")
        print(f"{parte_real:.2f} - {parte_imaginaria:.2f}i")

