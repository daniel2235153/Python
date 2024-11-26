# Escribir una función sumar() y una función multiplicar(), estas deben sumar y multiplicar
#  respectivamente todos los números de una lista. #Por ejemplo: sumar([1,2,3,4]) debería devolver 10 
# y multiplicar([1,2,3,4]) debería devolver 24.
def sumar(lista):
    total = 0
    for num in lista:
        total += num
    print("El resultado de la suma es ",total)
    # Tiene que imprimir 36

def multiplicar(lista):
    resultado = 1
    for num in lista:
        resultado *= num
    print("El resultado de la multipliacion es",resultado) 
    # Tiene que imprimir 10395

lista = [1, 3, 5, 7, 9, 11]

multiplicar(lista)  
sumar(lista)  