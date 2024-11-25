#Ej:2 Diseñe una función llamada area_perimetro_circulo(radio) que devuelva el perimetro 
# y área de un círculo a partir de un radio
import math
def area_perimetro_circulo():
    radio = float(input("Ingresa el radio del círculo: "))
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro

area, perimetro = area_perimetro_circulo()

print(f"Área del círculo: {area}")
print(f"Perímetro del círculo: {perimetro}")
