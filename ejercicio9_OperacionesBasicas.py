#Elabore un programa que sirva para hallar el perimetro y área de  un triangulo rectángulo. Solicite todos los datos necesarios por pantalla y el usuario los debe ingresar. Al finalizar el programa debe imprimir la información de los mismos. 
import math
print("CALCULADORA DE TRIANGULOS RECTANGULOS: ")
print("Digite el cateto opuesto")
cOp= float(input())
print("Digite el cateto adyasente")
cAd= float(input())
hip= math.sqrt(cOp**2 +cAd**2)
per= cOp + cAd + hip
area= (cAd *cOp)/2
print("La hipotenusa es:",hip)
print("Perimetro del triangulo:",per,"\nArea del triangulo:",area)
