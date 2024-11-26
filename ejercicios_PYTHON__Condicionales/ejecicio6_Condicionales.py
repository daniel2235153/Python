#EJ.6 Escriba un programa que permita al usuario elegir un candidato por el cual votar. Las posibilidades son:
#  candidato A, candidato B, candidato C y voto 
#en blanco. Según el candidato elegido (A, B, C ó Voto blanco) se le debe imprimir el mensaje “Usted ha votado por el candidato #”. 
#Si el usuario ingresa una opción que no corresponde a ninguno de los candidatos disponibles, indicar “Opción errónea”.

while True:
    print('''IIngrese el Candidato por el que desea votar:
    1.Candidato A
    2.Candidato B
    3.Candidato C
    4.Voto en blanco\n''')

    opciones = {
        '1':'Candidato A','2':'Candidato B','3':'Candidato C','4':'Voto en blanco'}
    while True:
        voto = input('Ingrese la opción a votar: ')
        if voto in opciones:
            break
        else:
            print('Opcion erronea')

    print(f'Usted ha votado por {opciones[voto]}') 
