#EJ.5 Escriba un programa que me permita cambiar unidades de longitud. 
# Su programa debe solicitar escoger en que unidad va ingresar la medida y en que unidad 
#la quiere visualizar en pantalla, su programa debe disponer de conversiones 
# (metro, kilómetros, centímetros, millas, yardas, pies o pulgadas). 
#Ejemplo: pida una distancia en pulgadas o pies y que escriba esa distancia en centímetros. 
# Se recuerda que una pulgada son 2,54 cm y un pie son doce pulgadas.

print('''Ingrese el tipo de medidia:
1.Metro
2.Kilometros
3.Centimetros
4.Millas
5.Yardas
6.Pies
7.Pulgadas\n''')

opciones = ['1','2','3','4','5','6','7']
while True:
    op = input('Ingrese el tipo de dato: ')
    if op in opciones:
        break
    else:
        print('!INGRESE UNA OPCION VALIDA!!')
 
while True:
    try:
        d0 = float(input('Ingrese el valor de la medida: '))
        break  
    except ValueError:
        print('!!INGRESE UN VALOR NUMERICO')
print('\n')

if op == '1':
    f0 = d0
elif op == '2':
    f0 = d0*1000
elif op == '3':
    f0 = d0/100
elif op == '4':
    f0 = d0*1609.34 
elif op == '5':
    f0 = d0*0.9144
elif op == '6':
    f0 = d0*0.3048
elif op == '7':
    f0 = d0*0.0254


print('''INGRESE LA MEDIDA A LA QUE DESEA CONVERTIR:
1.Metro
2.Kilometros
3.Centimetros
4.Millas
5.Yardas
6.Pies
7.Pulgadas\n''')

while True:
    v1 = input('Ingrese el tipo que quiere como respuesta: ')
    if v1 in opciones:
        break
    else:
        print('!INGRESE UNA OPCION VALIDA!!')
print('\n')

if v1 == '1':
    f1 = f0
elif v1 == '2':
    f1 = f0/1000
elif v1 == '3':
    f1 = f0*100
elif v1 == '4':
    f1 = f0/1609.34 
elif v1 == '5':
    f1 = f0*1.09361
elif v1 == '6':
    f1 = f0*3.28084
elif v1 == '7':
    f1 = f0*39.3701

print(f'La conversion da {f1}')