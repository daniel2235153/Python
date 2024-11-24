#EJ.4 Diseñe un programa empleando las condiciones if-elif-else. Dicho algoritmo debe ser para hacer un menú de acceso a una calculadora. 
#Incluya todas las operaciones aritméticas, comparar números pares e impares , sacar porcentajes, hallar valores de razones trigonométricas.


import math as m
print('''PERIMETRO Y AREA DE FIGURAS GEOMETRICAS
 MARQUE: 1.Suma
         2.Resta
         3.Multiplicación
         4.División
         5.Comparar
         6.Porcentajes
         7.Razones Trigonometicas''')
while True:
     op = input('Ingrese la opción con la que desea trabajar: ')
     if op == '1':
         n1 = float(input('Ingrese un número: '))
         n2 = float(input('Ingrese otro número: '))
         print(f'La operacion {n1} + {n2} = {n1+n2}')
         break
     elif op == '2':
         n1 = float(input('Ingrese un número: '))
         n2 = float(input('Ingrese otro número: '))
         print(f'La operacion {n1} - {n2} = {n1-n2}')
         break
     elif op == '3':
         n1 = float(input('Ingrese un número: '))
         n2 = float(input('Ingrese otro número: '))
         print(f'La operacion {n1} * {n2} = {n1*n2}')
         break
     elif op == '4':
         n1 = float(input('Ingrese un número: '))
         n2 = float(input('Ingrese otro número: '))
         print(f'La operacion {n1} / {n2} = {n1*(1/n2)}')
         break
     elif op == '5':
         n1 = float(input('Ingrese un número: '))
         if n1 % 2 == 0:
             print(f'El número {n1} es un número par')
             break
         else:
             print(f'El número {n1} es un número impar')
             break
     elif op == '6':
         n1 = float(input('Ingrese un número: '))
         n2 = float(input('Ingrese el porcentaje que desea sacar: '))
         print(f'El  {n2}% de {n1} es {(n2/100)*n1}')
         break
     elif op == '7':
         print('Considere el numero en radianes')
         n1 = float(input('Ingrese un número: '))
         razon = input('''Ingrese la opción de la razón trigonométrica a tratar: 
         1.sin(x)
         2.cos(x)
         3.tan(x)\n''')
         if razon == '1':
             print(f'El sin({n1}) es {round(m.sin(n1),3)}')
             break
         elif razon == '2':
             print(f'El cos({n1}) es {round(m.cos(n1),3)}')
             break
         else:
             print(f'La tan({n1}) es {round(m.tan(n1),3)}')
             break
     else:
         print('DIGITE UNA OPCIÓN ADECUADA')

