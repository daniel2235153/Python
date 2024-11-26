# Implemente un algoritmo usando Python y paquetes Numpy o Sympy para resolver la siguiente situación. 
# Unos estudiantes de ingeniería electrónica están implementando este circuito en protoboard y deben 
# comprobar los datos obtenidos en el laboratorio. Los datos por comprobar son corriente que genera 
# la fuente de voltaje y potencia de consumo. Se debe ingresar el código del estudiante y su algoritmo 
# organizar la información así: Vb = suma de su código de estudiante R1= suma de las tres primeras cifras 
# de su código R2= suma de la segunda, tercera y cuarta cifra de su código R3= suma de la tercera, cuarta y 
# quinta cifra de su código R4= suma de la cuarta, quinta y sexta cifra de su código R5= suma de las tres 
# últimas cifras de su código. Si llega a presentarse que una resistencia sume cero, este valor será reemplazado 
# por 10 ohmios.  Uso de matrices es requisito para la solución del ejercicio
import numpy as np
from sympy import symbols, Eq, solve

def obtener_valores(codigo):
    """
    Calcula los valores de Vb, R1, R2, R3, R4 y R5 a partir del código de estudiante.
    """
    digitos = [int(d) for d in codigo]

    Vb = sum(digitos)  
    R1 = sum(digitos[:3])  
    R2 = sum(digitos[1:4])  
    R3 = sum(digitos[2:5])  
    R4 = sum(digitos[3:6])  
    R5 = sum(digitos[-3:])  

    
    R1 = R1 if R1 != 0 else 10
    R2 = R2 if R2 != 0 else 10
    R3 = R3 if R3 != 0 else 10
    R4 = R4 if R4 != 0 else 10
    R5 = R5 if R5 != 0 else 10

    return Vb, R1, R2, R3, R4, R5


def resolver_circuito(Vb, R1, R2, R3, R4, R5):

    I1, I2, I3 = symbols('I1 I2 I3')

    eq1 = Eq(Vb - I1 * R1 - I3 * R3, 0)  
    eq2 = Eq(Vb - I1 * R1 - I2 * R2, 0)  
    eq3 = Eq(I1 - I2 - I3, 0)            

    soluciones = solve([eq1, eq2, eq3], (I1, I2, I3))
    
    potencia = (soluciones[I1]**2 * R1 +
                soluciones[I2]**2 * R2 +
                soluciones[I3]**2 * R3 +
                (soluciones[I2] - soluciones[I3])**2 * R4 +
                soluciones[I2]**2 * R5)

    return soluciones, potencia


def main():
    print("=== Cálculo de circuito eléctrico ===")
    codigo = input("Ingrese su código de estudiante (al menos 6 dígitos): ").strip()

    if len(codigo) < 6 or not codigo.isdigit():
        print("El código debe tener al menos 6 dígitos y solo contener números.")
        return
    Vb, R1, R2, R3, R4, R5 = obtener_valores(codigo)

    print(f"\nValores calculados:")
    print(f"Vb = {Vb} V")
    print(f"R1 = {R1} Ω, R2 = {R2} Ω, R3 = {R3} Ω, R4 = {R4} Ω, R5 = {R5} Ω")

    soluciones, potencia = resolver_circuito(Vb, R1, R2, R3, R4, R5)

    print(f"\nCorrientes en el circuito:")
    for corriente, valor in soluciones.items():
        print(f"{corriente} = {valor:.4f} A")

    print(f"\nPotencia total consumida: {potencia:.4f} W")



main()
