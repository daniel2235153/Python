#EJ.7 Diseñe un algoritmo que le permita crear una lista con nombres de estudiantes (N nombres), 
# su programa debe permitir buscar si los nombres están 
#contenidos en la lista, la consulta solicita nombres y verifica si están o no. Recomiendo uso for e if

while True:
    try:
        n = int(input('Ingrese la cantidad de nombres que desea: '))
        break
    except ValueError:
        print('Ingrese un valor valido')
lista = []
for i in range(n):
    name = input(f'Ingrese el {i+1}° nombre: ')
    lista.append(name)
print(lista)

Buscar = input('Ingrese el nombre que desea consultar: ')

if Buscar in lista:
    for j in range(n):
        if Buscar == lista[j]:
            print(f'El nombre se encuenta en la posicion {j+1} de la lista')
else:
    print(f'El nombre {Buscar} no se encuentra en la lista de estudiantes ingresada')

