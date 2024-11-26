#Empleando el condicional IF realice el diseño de un algoritmo que solicite por pantalla los datos de unos empleados: 
# Nombre y Apellido, documento de identidad, sueldo. Con estos datos su programa debe saber que personas ganan superior 
# al salario mínimo y mostrar al finalizar la ejecución los datos del empleado e indicar si gana o no superior al salario 
# mínimo en Colombia. 

numTrabaj = input('Ingrese la cantidad de empleados: ') 
lis_trabaj = []

salario_minimo = 1300000

for i in range(int(numTrabaj)):
    print(f"\nIngrese los datos del empleado {i + 1}:")
    name = input("Nombre completo: ")
    Cc = input("Número de Documento: ")
    salario = int(input("Salario: "))
    
    person = [name, Cc, salario]
    lis_trabaj.append(person)

print("\n--- Resultados ---")
for empleado in lis_trabaj:
    nombre = empleado[0]
    documento = empleado[1]
    salario = empleado[2]
    if salario >= salario_minimo:
        print(f"{nombre}  (Documento: {documento}) gana superior al salario mínimo.")
    else:
        print(f"{nombre}  (Documento: {documento}) no gana superior al salario mínimo.")

