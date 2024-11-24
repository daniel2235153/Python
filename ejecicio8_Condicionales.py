#EJ.8 Escribir un programa que permita al usuario ingresar por teclado 5 números enteros, que pueden ser positivos o negativos. Al finalizar, 
#mostrar la sumatoria de los números negativos y el promedio de los positivos. Recuerde que no es posible dividir por cero, por lo que es
#necesario evitar que el programa arroje un error si no se ingresaron números positivos.'''

lista_p = []
lista_n = []

for i in range(5):
    while True:
        try:
            num = int(input(f'Ingrese el {i+1}° número: '))
            if num < 0:
                lista_n.append(num)
                break
            else:
                lista_p.append(num)
                break                
        except ValueError:
            print('Tiene que ser un numero entero')
print(f'La suma de los numeros negativos es: {sum(lista_n)}')
print(f'El promedio de los numeros postivos es: {round(sum(lista_p)/len(lista_p),3)}')