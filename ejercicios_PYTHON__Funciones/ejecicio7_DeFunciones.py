#Diseñe un algoritmo que realice el proceso de ordenar una lista dada con números enteros y estos
#se repartan en dos listas pares e impares respectivamente. Cree una función Separar(lista). 
#Utilice los comandos nombrelista.sort() para ordenar la lista y nombrelista.append()
def Separar(lista):
    pares = []
    impares = []

    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    pares.sort()
    impares.sort()

    print(f"Lista original: {lista}")
    print(f"Números pares ordenados: {pares}")
    print(f"Números impares ordenados: {impares}")

numeros = [7, 2, 9, 4, 6, 3, 1, 8, 5,12,14,15,17,400]
Separar(numeros)
