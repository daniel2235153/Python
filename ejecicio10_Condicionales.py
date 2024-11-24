#EJ.10 Escribir un programa que le diga al usuario que ingrese una cadena. 
# El programa tiene que evaluar la cadena y decir cuántas letras mayúsculas tiene.
s = input('Ingrese una cadena: ')
Mayus = 0
for i in s:
    if i.isupper():
        Mayus = Mayus + 1
print(f'La cadena {s} tiene {Mayus} mayusculas')
