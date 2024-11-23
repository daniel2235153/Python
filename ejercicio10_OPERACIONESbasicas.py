#Elabore un programa que sirva para hallar el perimetro y área de  un circulo.
#  Solicite todos los datos necesarios por pantalla y el usuario los debe ingresar. 
# Al finalizar el programa debe imprimir la información de los mismos. 
import math
print("CALCULADORA DE CIRCULOS: ")
print("Digite el Radio del circulo")
r=float(input())
per= (2)* (math.pi)* (r)
area= (math.pi)* (r**2)
print("perimetro del circulo:",per,"\nArea del circulo:", area)