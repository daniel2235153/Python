def Separar(lista):
    # Crear listas para pares e impares
    pares = []
    impares = []
    
    # Separar números en las listas correspondientes
    for num in lista:
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    # Ordenar las listas
    pares.sort()
    impares.sort()
    
    # Imprimir los resultados
    print(f"Lista original: {lista}")
    print(f"Números pares ordenados: {pares}")
    print(f"Números impares ordenados: {impares}")


# Ejemplo de uso
numeros=int(input("Digite varios numeros"))
Separar(numeros)
