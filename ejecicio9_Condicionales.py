#EJ.9 Escriba un programa que pida números enteros mientras sean cada vez más grandes,
#  al digitar un número menor que el anterior debe imprimir 
#un mensaje diciendo que ese número es menor y terminar el programa usando while.

a = [0]
while True:
    try:
        entrada = int(input('Ingrese un numero: '))
        break
    except ValueError:
        print('Digite el valor correctamente')
posicion = 0
while entrada >= a[posicion]:
    a.append(entrada)
    posicion += 1
    entrada = int(input('Ingrese un numero: '))
    while entrada <= a[posicion]:
        print('Digite un numero mayor')
        break