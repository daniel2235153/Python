#EJ.3 Escribir un programa que solicite al usuario una letra. Al ingresarla por teclado si es una vocal, muestre el mensaje “es vocal”. 
#Se debe validar que el usuario ingrese sólo un carácter. Al ingresar un string de más de un carácter, informarle que no se puede 
# procesar el dato.

num = [str(i) for i in range(10)] 
vocals = ['a', 'e', 'i', 'o', 'u']

while True:
    vocal = input('Ingrese un caracter: ')
    if len(vocal) == 1:
        if vocal in num:
            print('Usted digitó un número')
            break
        elif vocal.lower() in vocals:
            print('Usted digitó una vocal')
            break
        else:
            print('Usted no digitó una vocal')
            break
    else:
        print('Digite solo un caracter')
