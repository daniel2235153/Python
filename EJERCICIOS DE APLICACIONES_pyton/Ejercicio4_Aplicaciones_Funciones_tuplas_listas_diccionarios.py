
n = []
pares = []
impares = []
print("Introduce números para llenar la lista O escribe '0' para terminar:")
while True:
    try:
        numero = int(input("Número: "))
        if numero == 0:
            break
        n.append(numero)
    except ValueError:
        print("Por favor, ingresa un número válido.")

n.sort()
print(f"\nLista ordenada: {n}")

for numero in n:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
