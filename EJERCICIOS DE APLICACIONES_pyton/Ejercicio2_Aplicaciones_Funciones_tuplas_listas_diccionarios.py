#Crea una tupla con los meses del año, su programa debe solicitar por pantalla números al usuario, 
# si el número esta entre 1 y la longitud máxima de la tupla (12), muestra el contenido de esa posición 
# sino muestra un mensaje de error. El programa termina cuando el usuario introduce un cero.
meses= ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio","Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
print("Hola")

while True:
    a=int(input("Digite un numero entre (1 y 12)"))
    if a==0:
        break
    elif 1 <= a <= len(meses):
        print(f"El mes correspondiente es: {meses[a - 1]}")
    else:
        print("Error: El número debe estar entre 1 y 12.")


